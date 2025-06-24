import azure.cognitiveservices.speech as speechsdk
import google.generativeai as genai
import os   
# from openai import OpenAI
# Replace with your Azure credentials
speech_key = os.environ.get("AZURE_SPEECH_API_KEY")
service_region = os.environ.get("AZURE_SERVICE_REGION", "eastasia")
gemini_api_key = os.environ.get("GEMINI_API_KEY")
service_region = "eastasia"


speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# === STEP 1: Transcribe first voice input ===
def transcribeAudio(file_path):
    audio_config = speechsdk.AudioConfig(filename=file_path)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    print("Transcribing initial audio...")
    result = recognizer.recognize_once()
    print("Transcribed Text:", result.text)
    return result.text

# === STEP 2: Pronunciation assessment using transcript ===
def assessPronunciation(audio_path, reference_text):
    audio_config = speechsdk.AudioConfig(filename=audio_path)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    pron_config = speechsdk.PronunciationAssessmentConfig(
        reference_text=reference_text,
        grading_system=speechsdk.PronunciationAssessmentGradingSystem.HundredMark,
        granularity=speechsdk.PronunciationAssessmentGranularity.Word,
        enable_miscue=True
    )
    pron_config.apply_to(recognizer)

    print("Evaluating pronunciation...")
    result = recognizer.recognize_once()
    json_result = result.properties[speechsdk.PropertyId.SpeechServiceResponse_JsonResult]
    print(json_result)
    return json_result

# === STEP 3: Evaluate the transcript based on the exam's question
# def assessTranscript(question, transcript, json_result):
#     client = OpenAI(api_key = openai_api_key)
#     prompt = (
#         f"Dựa vào câu hỏi này trong phần Speaking của bài thi VSTEP: \"{question}\", "
#         f"hãy đánh giá mức độ liên quan của đoạn văn thí sinh trả lời: \"{transcript}\" với đề bài. "
#         f"Dựa vào kết quả trong file json sau, đánh giá lỗi sai của thí sinh đó: {json_result}"
#     )

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",  # or "gpt-4" if available
#         messages=[
#             {
#                 "role": "system",
#                 "content": (
#                     "You are a professional English-speaking evaluation assistant. Your job is to assess users' spoken English "
#                     "based on pronunciation, fluency, grammar, vocabulary usage, and coherence. Provide objective, constructive, "
#                     "and clear feedback. When necessary, offer specific suggestions for improvement. Assume the user may be "
#                     "preparing for VSTEP exam, and tailor your feedback accordingly."
#                 )
#             },
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )

#     return response.choices[0].message.content
def assessTranscript_G(question, transcript, json_result):
    genai.configure(api_key = gemini_api_key)
    prompt = (
        f"Dựa vào câu hỏi này trong phần Speaking của bài thi VSTEP: \"{question}\", "
        f"hãy đánh giá mức độ liên quan của đoạn văn thí sinh trả lời: \"{transcript}\" với đề bài. "
        f"Dựa vào kết quả trong file json sau, đánh giá lỗi sai của thí sinh đó: {json_result}."
        "Gọi \"thí sinh\" là \"bạn\". Không giới thiệu bản thân là trợ lý đánh giá. Không đề cập tới từ \"JSON\". Không cần nhắc lại đề bài và câu trả lời của thí sinh. Không cần đưa ra lời khuyên cho kỳ thi VSTEP, chỉ cần đánh giá kết quả đầu vào."
    )

    system_instruction = (
        "You are a professional English-speaking evaluation assistant. Your job is to assess users' spoken English "
        "based on pronunciation, fluency, grammar, vocabulary usage, and coherence. Provide objective, constructive, "
        "and clear feedback. When necessary, offer specific suggestions for improvement. Assume the user may be "
        "preparing for the VSTEP exam, and tailor your feedback accordingly."
    )

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content([
        {"role": "user", "parts": [system_instruction]},
        {"role": "user", "parts": [prompt]}
    ])

    return response.text

# === Example Usage ===
# Step 1: Get transcript from first spoken audio
# reference_text = transcribeAudio("voice_f.wav")  # <-- First input
# print(reference_text)

# # Step 2: Evaluate pronunciation based on that transcript
# assessPronunciation("voice_f.wav", reference_text)  # <-- Second input



# user_input = input("Enter your question: ")

