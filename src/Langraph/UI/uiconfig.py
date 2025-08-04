from configparser import ConfigParser


class Config:
    def __init__(self, config_file='src/Langraph/UI/uiconfig.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        return self.config.get('DEFAULT', 'PAGE_TITLE', fallback='LangGraph')

    def get_llm_options(self):
        return self.config.get('DEFAULT', 'LLM_OPTIONS', fallback='Groq').split(',')

    def get_usecase_options(self):
        return self.config.get('DEFAULT', 'USECASE_OPTIONS', fallback='AGENTIC CHATBOT, AI NEWS, BLOG GENERATOR, CHATBOT WITH TOOL').split(',')

    def get_groq_model_options(self):
        return self.config.get('DEFAULT', 'GROQ_MODEL_OPTIONS', fallback='gemma2-9b-it , meta-llama/llama-4-scout-17b-16e-instruct').split(',')
