import os

def simple_chatbot():
    print("Namaste! Main ek simple chatbot hoon. Main aapke file system ke saath bhi kaam kar sakta hoon.")
    print("Mujhse baat karne ke liye 'exit' type karke chat khatam kar sakte hain.")

    while True:
        user_input = input("Aap: ")
        
        # Convert user input to lowercase for easier processing
        processed_input = user_input.lower()
        if "namaste" in processed_input or "hello" in processed_input:
            print("Bot: Namaste! Kaise hain aap?")
        elif "kaise ho" in processed_input or "how are you" in processed_input:
            print("Bot: Main theek hoon, aapka shukriya. Aap kaise hain?")
        elif "kya kar rahe ho" in processed_input or "what are you doing" in processed_input:
            print("Bot: Main aap se baat kar raha hoon. Aapka din kaisa raha?")
        elif "kya naam hai tumhara" in processed_input or "what is your name" in processed_input:
            print("Bot: Mera koi naam nahi hai, main ek program hoon.")
        
        # --- OS Library Functionality ---
        elif "folder banao" in processed_input or "create folder" in processed_input:
            print("Bot: Theek hai, main ek folder bana raha hoon. Folder ka naam kya doon?")
            folder_name = input("Folder ka naam: ")
            try:
                os.mkdir(folder_name)
                print(f"Bot: '{folder_name}' naam ka folder ban gaya hai. 📂")
            except FileExistsError:
                print(f"Bot: Maaf kijiye, '{folder_name}' naam ka folder pehle se hi maujood hai.")
            except Exception as e:
                print(f"Bot: Maaf kijiye, ek galti hui: {e}")

        elif "list files" in processed_input or "list files" in processed_input:
            print("Bot: Theek hai, main is directory mein files aur folders ki list dikha raha hoon.")
            files = os.listdir('.')
            if files:
                for item in files:
                    print(f"-> {item}")
            else:
                print("Bot: Is directory mein koi files ya folders nahi hain.")

        # --- Basic Chatbot Functionality (pehle wala code) ---
        elif "mausam kaisa hai" in processed_input or "weather" in processed_input:
            print("Bot: Maaf kijiye, main mausam ki jaankari nahi de sakta. Main bas aapse baat kar sakta hoon.")
        elif "python" in processed_input:
            print("Bot: Python ek bohot hi shandaar programming language hai. Isi se main bana hoon.")
        elif "exit" in processed_input or "alvida" in processed_input:
            print("Bot: Aapse baat karke achcha laga. Alvida!")
            break
        else:
            print("Bot: Maaf kijiye, main is baat ko nahi samajh paya. Koi aur baat poochiye?")

# Run the chatbot
simple_chatbot()