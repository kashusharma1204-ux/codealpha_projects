from datetime import datetime

print(" Simple Chatbot ")
hello_count=0
while True:
    user = input("You: ").lower()

     
    if user == "hello":
        hello_count+=1
        if hello_count == 1:
         print("Bot: Hi! how can i help you Today") 
        else:
            print("Bot: Hi again! how can i help you Today")    

    elif user == "hi":
        print("Bot: Hello! buddy")

    elif user == "how are you":
        print("Bot: I am fine. What about you?")

    elif user == "i am fine":
        print("Bot: Nice to hear that!")

    elif user == "what is your name":
        print("Bot: I am a chatbot")
        
    elif user == "why are you made":
        print("i was made to assist people like you by providing information,answering questions, and having engaging conversations. my goal is to be a helpful and friendly AI")  
        
    elif user == "good morning":
        print("Bot:good morning! I hope you have a wonderful day ahead")
        
    elif user == "good afternoon":
        print("Bot:good Afternoon! I hope you're having a great day")   

    elif user == "good evening":
        print("Bot:good evening! how are you doing?")
        
    elif user == "what is time":
      current_time = datetime.now()
      print("Bot:", current_time.strftime("%I:%M %p"))  
     
    elif user =="what is date":
        current_date = datetime.now()
        print("Bot:", current_date.strftime("%d-%m-%Y"))
   
    elif user == "bye":
        print("Bot: Goodbye! have a nice day")
        break

    else:
        print("Bot: Sorry, I don't understand.")