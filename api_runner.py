from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def get_response(prompt, max_retry=5):

    for attempt in range(max_retry):

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text.strip()

        except Exception as e:
            error_str = str(e)

            if "503" in error_str or "UNAVAILABLE" in error_str:
                wait = 2 ** attempt  # 1 → 2 → 4 → 8 → 16초
                print(f"에러 발생: {e}")
                print(f"재시도 중... {wait}초 대기 ({attempt+1}/{max_retry})")
                time.sleep(wait)

            else:
                # 503 아닌 에러(인증 실패, 잘못된 요청 등)는 재시도 의미 없음
                print(f"복구 불가 에러: {e}")
                raise e

    print("최대 재시도 횟수 초과")
    return "ERROR"