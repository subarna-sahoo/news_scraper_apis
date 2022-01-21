from firebase_admin import credentials, firestore, auth
import firebase_admin

firebaseConfig = {
  "type": "service_account",
  "project_id": "news-420bf",
  "private_key_id": "997a11bebb06f459238b9cb5e5a58a238b5e8f26",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCxSVXZkn8zDDo8\nx1ooAFBzdUd6BvNn3/ZZ8c4+S2Dgc7Urg6UO9IvOKaBQn65l1zdM7QMkJ7btArS8\nnW+9SdfhNUWOqxXXNu0/dU9+Wa1B2A5DkzSaLBjA8+5qaRNJtum4nEywnmD1sYxb\nXRAAIwWpM3hgbJRg7vNeD2Dw0pm8qvawyXMSLzmspivpcdJJtK0rJT3L57M5BvsN\nGQzxfOmf51HiMeyWOYDLCd3u90XPsvlo5nODWfrhqyj+QOYdAYUcRM1HUmf7214L\nBwi/1HpwW/+K+BDe0OXHaW2yj6r2le/xTQn2dzSWt3qy4ltPhDy9lJVuahWBZy/K\nFeGNgbVxAgMBAAECggEAGI1DamIzY2pqFki1X5zLh3HSeD/GLbiCcWpfWZkuzWa4\nzFHq5etQATkajo/OoyPu8KRSLwug9anOReC3vMshLnsmKt/eonNk38jrPWBF8jxt\nnUYhnshElVQyzGHI3giKzZo3tK36V4xDF9QHhz1SZ2BNZ20iD1qIMZqHnlJMICiB\n/SIjzC3T1bvo6eVZEv1pyomOtCVUm7uK0SQ2erxMaABVBS4MfgBPsDlmaKkfu1SU\noDgkvMQl89f9lvK4O0u3oix76RJ1QH+hviz86Q5JbLn7A1fsFPS6QY1kHJ8exvHW\nd2MALscL/qeifSO01S1RD72EcqpIDZbjGsj6rIvjUQKBgQDdJ6DGL6/V26qaKWuE\nIKIzPIAV9Hy2gV6Qi+WV+Q7OqvNX7rPgjKDBz4f71ntI5/8D62C0+IJhHjfj5dSv\n8z+71xVo421SINYUe4ZoBcfqVgqaYj6RvXiKHvLzVTgAXbC7dnRQ8gXETn+0J4/R\nfa4WF+XBJM0bMhkukf9/YyDtnwKBgQDNOEJ8att0afsLGVF50G8ySiokLts6EHJp\n69kaQgbIIoN2BBqZ2222R6IwkFFUOAaMUJisA21bCHHDQ4NdJMtLMPxzA3m5JI7C\nAbeZcsQsDglrjYHj27WS4MW/PnM2cSngKj+Euq1iIYeCtux9KInRbzqAVzAjRNeE\n1reRvBNi7wKBgBYcGB64NcQTqgKvkWgsOwsUSVnoj29Pj7yzv8g2lhxjSuDHpIQW\nixvVO6sZzkmDqCMkLQ7qqV48PyoxmAnfL8f/wMwzsII9dimmD9Hmgg4TfAvjNo4r\nexmT7oYVRvwCYeDb/tT43Uq67ll8ewxenEDpMrcUjszhPVNClWCO8IPRAoGBAIlv\nbgdIwOO7viZ2tDvyPSXeyU4mGydNsHIDQwf0w/nwMz4sDWyQqW7zlkkTvYO7aZc6\nuqQoP2pBw35TjnwokgUvL0IPR8uYEgsXf0/CrmIanHBs+loQ4A8XfRdQyXPiYXsA\nkD1hj5AyiEAgJUzEg1fBN9qPiWt1RShva8yrugf9AoGAd/vtXPdqK3tvOUZrcZbK\nVD8dg8N5Mv3QX1LFCQHG9XCxNpudpXxNr6/pWAe1KYns+M2vrEXc60HRbpJLumA+\nYdjIxYcVbVcj/nMmU+bspUJKtQl8ZvJSaAIU7sN3iwzPjaaAdtLKt8knkpsFMjrC\nBLvmDpCbPxVaHKM7m2M5d3k=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-dy7dy@news-420bf.iam.gserviceaccount.com",
  "client_id": "114652399472716967201",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-dy7dy%40news-420bf.iam.gserviceaccount.com"
}


cred = credentials.Certificate(firebaseConfig)
firebase_admin.initialize_app(cred)
db = firestore.client()
