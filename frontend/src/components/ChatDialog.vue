<script setup lang="ts">
import { ref } from 'vue'
import api from '@/api'
import ChatMessage from '@/components/ChatMessage.vue'

interface Message {
    role: string;
    content: string;
}

const greeting = 'Hi, I am Agent IQ! How can I help you?'
const props = defineProps<{ visible: boolean }>()
const emit = defineEmits(['close'])
const messages = ref<Message[]>([{ role: 'agent', content: greeting }])
const input = ref('')
const waiting = ref(false)
const session_id = ref<number | undefined>()

async function send() {
    if (!input.value.trim()) return
    waiting.value = true
    let userInput = input.value
    input.value = ''
    messages.value.push({ role: 'user', content: userInput })

    try {
        const response = await api.post('/chat', { content: userInput, session_id: session_id.value }, {
            responseType: 'stream',
            adapter: 'fetch'
        })

        const reader = response.data.getReader()
        const decoder = new TextDecoder()

        while (true) {
            const { done, value } = await reader.read()
            if (done) break

            const chunk = JSON.parse(decoder.decode(value, { stream: true }))
            session_id.value = chunk.session_id
            messages.value.push({ role: 'agent', content: chunk.content })
        }
    } catch (error) {
        console.log("Chat error:", error)
        messages.value.push({ role: "agent", content: "Sorry, something went wrong. Please try again." })
    }

    waiting.value = false
}

function newSession() {
    messages.value = [{ role: 'agent', content: greeting }]
    session_id.value = undefined
}
</script>

<template>
    <Dialog :visible="props.visible" position="bottomright" header="Agentiq Chat" :style="{ width: '25rem' }"
        @update:visible="$emit('close')">
        <ChatMessage v-for="message in messages" :role="message.role" :message="message.content" />
        <template #footer>
            <div>
                <div class="flex items-end border-solid border-2 rounded-lg dark:bg-gray-950">
                    <Textarea v-model="input" rows="2" cols="40" autoResize fluid class="border-none outline-none" />
                    <Button rounded variant="text" @click="send" :disabled="waiting">
                        <fa-icon icon="fa-solid fa-arrow-up" />
                    </Button>
                </div>
                <Button label="New Session" variant="text" size="small" class="p-0 mt-3" @click="newSession" />
            </div>
        </template>
    </Dialog>
</template>
