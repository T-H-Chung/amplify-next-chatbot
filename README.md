# Amplify Next Chatbot
### A decent assistant for Amplify Gen 2 applications that using Next.js and @aws-amplify/ui-react

**🤖 The chatbot is [Chainlit](https://docs.chainlit.io/get-started/overview) app built on a [GraphRAG](https://github.com/microsoft/graphrag) 
with [Amplify Gen 2](https://docs.amplify.aws/nextjs/), [Next.js](https://nextjs.org/docs), and [@aws-amplify/ui-react](https://ui.docs.amplify.aws/react) documentations**

### Why Amplify Next Chatbot?
- Amplify Gen 2 is very new, so ChatGPT might not be able to provide accurate answers, and there aren't many examples available online either. The same goes for `@aws-amplify/ui-react`.
- Amazon Q is a good tool, while it's difficult to build an application from scratch and heavily relies on other code within your repository.
It also cannot recognize or generate the UI you want to use, even if you've already imported `@aws-amplify/ui-react`.
By integrating it with this chatbot, you can build even better apps.
- Inheriting the benefits of GraphRAG, it offers higher accuracy and more comprehensive answers. Additionally, it enhances interpretability, traceability, and access control, which brings advantages in terms of governance.

## Quick Start
### Prerequisite
- Your own [OpenAI API key](https://platform.openai.com/api-keys) (You need to have a balance)
- Python >=3.10

### Installation and Configuration
1. Clone the repository
2. Install required Python packages:
  ```
  pip install -r requirements.txt
  ```
3. Create a `.env` file and put:
  ```
  GRAPHRAG_API_KEY=<Your OpenAI API key>
  ```
4. Run the command in ternimal:
  ```
  chainlit run app.py -w
  ```
