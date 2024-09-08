# Amplify Next Chatbot
### A decent assistant for Amplify Gen 2 applications that using Next.js and @aws-amplify/ui-react

**🤖 The chatbot is [Open WebUI](https://github.com/open-webui/open-webui) app built on a [GraphRAG](https://github.com/microsoft/graphrag) 
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
- Python >=3.11

### Installation and Configuration
#### On Server End
1. Clone the repository
2. Install required Python packages:
  ```
  pip install -r requirements.txt
  ```
3. Create a `.env` file and put:
  ```
  GRAPHRAG_API_KEY=<Your OpenAI API key>
  INPUT_DIR=output/20240906-224201/artifacts # default
  GRAPHRAG_LLM_MODEL=gpt-4o-mini # default
  ```
4. Run the command in ternimal:
  ```
  python main-en.py
  ```
#### On Client End
1. Install Open WebUI:
  ```
  pip install open-webui
  ```
2. Run the client interface:
  ```
  open-webui serve
  ```
3. Configure the settings
   1. Go to Connections tab in [Admin Settings](http://localhost:8080/admin/settings).
   2. Revise OpenAI API Base URL to `http://<your server location>:8012/v1` and set an arbitrary API Key.
  
4. (Optional) Select your Default Model(GraphRAG local or global method) at Interface tab of Settings.

## Credits
- Open WebUI interface of this project is revised from [the implementation by win4r](https://github.com/win4r/GraphRAG4OpenWebUI).
