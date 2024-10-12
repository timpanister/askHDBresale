# Methods

This is to document the steps i used to create the streamlit project.

1.  At command prompt, create a new project folder

2.  cd into folder

3.  Create virtual environment
        `python -m venv venv`

4.  Activate virtual environment `.\venv\Scripts\activate.bat`

5.  In the activated virtual environment, install the packages.

        pip install streamlit pandas openai python-dotenv pydeck  langchain langchain_experimental langchain-openai crewai crewai-tools

6. Create `requirements.txt` file at root of the project and add the Python libraries to it.

7.  Create a .streamlit folder at root of project folder

8.  In .streamlit folder, create a **secrets.toml** file. This will contain the password for launching the Streamlit app when deployed to online

        password = "12345"

9.  At root of project folder, create **.env** file with OPENAI key and model to use.

        OPENAI_API_KEY="key here"
        OPENAI_MODEL_NAME="gpt-4o-mini"

10.  Create a **.gitignore** file with the code below at the root.
        ```

                # Byte-compiled / optimized / DLL files
                __pycache__/
                *.py[cod]
                *$py.class

                # Virtual environments
                venv/
                env/
                ENV/
                .venv/
                .env

                # Distribution / packaging
                build/
                dist/
                *.egg-info/

                # VS Code
                .vscode/
                # PyCharm
                .idea/

                # Streamlit
                .streamlit/secrets.toml 
        ```

11. Copy the **helper_functions** folder from the AI Bootcamp

12. Create also a **pages** subfolder to the root. This will be the pages for the sidebar later. Unfortunately, I can't seem to be able to use this pages folder hack if I want to use the radio button navigation style, so my other pages are in the root folder

13. Create a **main.py** at the root of the project folder. This will be the main entry point for the app.

14. The tree will look something like this:

15. I also experimented with lots of Bing Copilot to come up with the code for the UI/UX I want to achieve. For example, the radio button style sidebar look and configure the buttons to navigate to the appropriate page. Basically i use lazy chat.



