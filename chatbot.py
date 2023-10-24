import openai
import argparse

openai.api_key =""


def main():
    parser = argparse.ArgumentParser(description="Simple command line chatbot with GPT-4")

    parser.add_argument("--personality", type=str, help="A brief summary of the chatbot's personality", default="Friendly and helpful")

    args = parser.parse_args()

    initial_prompt = f"You are a conversational chatbot. Your personality is: {args.personality} "

    messages = [{"role": "system","content": initial_prompt }]

    while True:
        try:
            user_input = input("You: ")
            messages.append({"role": "user", "content" : user_input})
            res = openai.ChatCompletion.create(
            model ="gpt-4",
            messages = messages
            )

            messages.append(res["choices"][0]["message"].to_dict())
        
            print(res["choices"][0]["message"]["content"])

        except KeyboardInterrupt:
            print("exiting")
            break

    print(res)

if __name__ == "__main__":
    main()