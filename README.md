# hugging-face-api
## Models used
- [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2)
- [GPT2](https://huggingface.co/docs/transformers/model_doc/gpt2)

## Pre-Setup
### **Step 1: Update the `.env` File**
Create a `.env` file in the project root directory and add the following:
``` 
KEY_HUGGING_FACE="YOUR API KEY"
```

Replace the placeholders with your actual Hugging face API KEY.

## Installation and Setup Guide (Windows)

### 1. Set Up a Virtual Environment

To start, you'll need to create a virtual environment for the project. This helps isolate the project's dependencies from your system's Python installation.

- Open your terminal (Command Prompt or PowerShell).
- Navigate to your project directory:
  ```
  cd path\to\task_manager
  ```

### 2. Create a Virtual Environment

Next, create a new virtual environment with the following command:
  ```
  python -m venv venv
  ``` 
This will create a folder named `venv` inside your project directory, where all the project dependencies will be stored.

### 3. Activate the Virtual Environment

Activate the virtual environment to begin using it:
  ```
  venv\Scripts\activate
  ``` 
Once activated, your terminal prompt will change to show `(venv)`, indicating that the virtual environment is now active.

### 4. Install Project Dependencies

With the virtual environment active, install the required dependencies listed in the `requirements.txt` file:
  ```
  pip install -r requirements.txt
  ``` 
This will automatically install all the necessary libraries for your project.

### 5. Verify Installation

To ensure that the dependencies have been installed correctly, you can check the list of installed packages with:
  ```
  pip list
  ``` 
This should display all the libraries and their respective versions that are installed in the virtual environment.

### 6. Run Your Project

You are now ready to run your projects. Execute the appSingleMode.py script with the following command:
  ```
  streamlit run appSingleMode.py
  ```

Or execute the appSingleMode.py script with the following command:
  ```
  streamlit run appMultiMode.py
  ```
### 7. Deactivate the Virtual Environment

Once you are done working with the project, deactivate the virtual environment:
  ```
  deactivate
  ``` 
This will return your terminal session to the global Python environment.

---

By following these steps, you'll ensure that your project is set up correctly with all the necessary dependencies installed, isolated in a virtual environment for easy management.

## Preview of the projects

For this example we use the following inputs that can be helpfull to have:
```
  question: "What is the name of the spacecraft that landed the first humans on the Moon?"
  context: 'The Apollo program, also known as Project Apollo, was the third United States human spaceflight program carried out by NASA, which succeeded in landing the first humans on the Moon from 1969 to 1972. The Apollo program was designed to land humans on the Moon and bring them safely back to Earth. The first successful lunar landing occurred during the Apollo 11 mission, which launched on July 16, 1969, and landed on the Moon on July 20, 1969. The spacecraft that achieved this feat was called the Lunar Module, or LM, nicknamed "Eagle." The mission commander, Neil Armstrong, and lunar module pilot, Buzz Aldrin, became the first humans to walk on the Moon, while Michael Collins remained in orbit aboard the Command Module "Columbia."'
  ```

### appSingleMode.py 
![image](https://github.com/user-attachments/assets/3c3e36dd-609c-4727-8920-46810021c5a9)

### appMultiMode.py 

![image](https://github.com/user-attachments/assets/359d2307-d2f2-4263-951b-dd0c1139ebb0)
![image](https://github.com/user-attachments/assets/c099933c-9ba7-4f69-a84e-3abf07a98dc0)

