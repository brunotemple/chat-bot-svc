import { groq } from "@ai-sdk/groq"
import { streamText } from "ai"

// Allow streaming responses up to 30 seconds
export const maxDuration = 30

export async function POST(req: Request) {
  try {
    // Extract the messages from the body of the request
    const { messages } = await req.json()

    // Call Groq with Llama 3.1 model
    const result = streamText({
      model: groq("llama-3.1-8b-instant"),
      messages,
      system: "You are a helpful, friendly AI assistant. Provide concise and accurate responses.",
    })

    // Return the stream response
    return result.toDataStreamResponse()
  } catch (error) {
    console.error("Error in chat route:", error)
    return new Response(JSON.stringify({ error: "Failed to process chat request" }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    })
  }
}
