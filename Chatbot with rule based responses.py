import re
def customer_care_chatbot(user_input):
    user_input = user_input.lower()
    general_inquiry_pattern = re.compile(r"(can you help me with|I need assistance with) (.+)")
    order_status_pattern = re.compile(r"(what is the status of|where is) my order (.+)")
    order_cancellation_pattern = re.compile(r"(cancel|cancellation) my order (.+)")
    refund_inquiry_pattern =re.compile(r"(refund|refund status) for my order (.+)")
    contact_support_pattern = re.compile(r"(contact|speak to) support")
    greet_pattern =re.compile(r"(hello|hi|hey|good morning|good afternoon|good evening)")
    chatbot_identity_pattern = re.compile(r"(who are you|what are you)")
    order_status_info = {
        "12345" : {"product":"Smartwatch","status":"out for delivery","message":"Your order is expected to arrive by the end of the day"},
        "24680" : {"product":"Tablet","status":"shipped","message":"Your order is expected to reach within 5 business days"},
        "13579" : {"product":"Laptop","status":"processing","message":"Your order is currently in processing and will be dispatched soon"},
        "36912" : {"product":"Books","status":"delivered","message":"Your order has been delivered.If you have any issues, please contact our support team"}
    }
    refund_status_info ={
        "35553" : {"product":"shoes","status":"processed","message":"The refund has been processed and will be credited to your account within 3 business days"},
        "53335" : {"product":"bracelet","status":"under review","message":"Refund is under review. You will recieve an email with further details very soon"}
    }
    if greet_pattern.match(user_input):
        return "Hello! How can I assist you today?"
    elif general_inquiry_pattern.match(user_input):
        inquiry_match = general_inquiry_pattern.match(user_input)
        inquiry = inquiry_match.group(2).lower()
        return f"Of course! I can help you with {inquiry.capitalize()}. Please provide more details so I can assist you better."
    elif order_status_pattern.match(user_input):
        order_match = order_status_pattern.match(user_input)
        order_number = order_match.group(2)
        if order_number in order_status_info:
            product_name = order_status_info[order_number]["product"]
            status = order_status_info[order_number]["status"]
            message = order_status_info[order_number]["message"]
            return f"The status of your {product_name} order #{order_number} is: {status}. {message}"
        else:
            return f"I'm sorry,but I couldn't find information for order #{order_number}. Please double-check the order number or contact supprt for further assistance."
    elif order_cancellation_pattern.match(user_input):
        cancellation_match = order_cancellation_pattern.match(user_input)
        order_to_cancel = cancellation_match.group(2)
        return f"Sure! I've initiated the cancellation process for order #{order_to_cancel}. You will receive an email confirmation shortly."
    elif refund_inquiry_pattern.match(user_input):
        refund_match = refund_inquiry_pattern.match(user_input)
        order_for_refund = refund_match.group(2)
        if order_for_refund in refund_status_info:
            product_name = refund_status_info[order_for_refund]["product"]
            status = refund_status_info[order_for_refund]["status"]
            message = refund_status_info[order_for_refund]["message"]
            return f"The refund status for your {product_name} order #{order_for_refund} is {status}. {message}"
        else:
            return f"I'm sorry, but I couldn't find information for the refund status of order #{order_for_refund}. Please contact support for further assistance."
    elif contact_support_pattern.match(user_input):
        return "Sure! To contact our customer support, please call our toll-free number at 1-800-123-4567 or send an email to support@example.com."
    elif chatbot_identity_pattern.match(user_input):
        return "I'm a customer care chatbot here to assist you with your inquiries. How can I help you today?"
    elif "goodbye" in user_input:
        return "Goodbye! If you have more questions or need assistance, feel free to read out."
    else:
        return "Oops, I'm still learning and didn't quite get that. If you have a specific question, please ask again!"
print("Chatbot: Hello! I'm your customer care assistant. How can I assist you today?")
while True:
    user_input = input("You: ")
    if "goodbye" in user_input.lower():
        print("Chatbot: Goodbye! If you have more questions or need assistance, feel free to reach out.")
        break
    response = customer_care_chatbot(user_input)
    print("Chatbot:", response)