# Importing necessary modules
from classes.ui.pages import Page
from classes.ui.textelements import TextElement
from classes.ui.title import Title
from classes.ui.header import Header
from classes.widgets.chatbot import chatbot

# Page's main configuration
homePage = Page(name='Roundpizza', icon='🍕', pageLayout='centered')
Header.hide_header()
Title('🍕 Roundpizza')

# Page's content
TextElement.write_caption("Bem-vindos à Roundpizza!")
TextElement('---')

# Chatbot
chatbot()