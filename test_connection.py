import requests
import time

def test_api_monitor():
    print("Testing API Monitor connection...")
    try:
        response = requests.get('http://localhost:8080/metrics', timeout=5)
        if response.status_code == 200:
            print("✅ API Monitor is running!")
            print(f"Response length: {len(response.text)} characters")
            print("\nFirst few lines:")
            print('\n'.join(response.text.split('\n')[:10]))
        else:
            print(f"❌ API Monitor returned status: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API Monitor on port 8080")
        print("Make sure to run: python api_monitor.py")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_api_monitor()