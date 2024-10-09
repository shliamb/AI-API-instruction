## API: OpenAI + img, Gemini + img, Dall-e 3, Audio


**Super short:** Examples of accessing the API in the folder - API-python-exemples. Access and key can be obtained in telegram bot - https://t.me/myapi_aibot

**Очень коротко:** Примеры доступа к API в папке - API-python-examples. Доступ и ключ можно получить в telegram-боте - https://t.me/myapi_aibot


## API Requests:


- When accessing the API, the presence of the username field in the body is checked, it is checked for presence in the database, whether it is blocked and whether there are funds. Next, his API Key corresponding to this particular user is checked, so I can block and implement the simplest temporary blocking to tapping the API.

- При обращении к API, проверяется наличие в теле поля username, проверяется на наличие в базе, не заблокирован ли и есть ли средства. Далее проверяется его API Key соответствующий именно этому пользователю, так я смогу блокировать и осуществлять простейшую временную блокировку к простукиванию API.

- If the attempt to access the user's API was not successful (attempts without funds, the wrong key, the user is blocked..), then after 5 attempts (unsuccessful attempts will be entered into the database, reset to zero again upon successful login), the user is temporarily blocked, in order to reset it simply by name.

- Если попытка обращения к API пользователя была не успешной (попытки без наличия средств, не верный ключ, заблокирован пользователь..), то через 5 попыток (не успешные попытки будут вноситься в базу, при успешном входе снова обнуляться), пользователь временно блокируется, для того, что бы сбрасывать его просто по имени.



## Getting access to work with the API:

- Переходим в телеграм бот - https://t.me/myapi_aibot , нажимаем старт - регистрация выполнена, забираем доступы и какую то сумму тестовую на балансе, читаем инструкцию и можно уже обращаться через постман или писать приложение, прикручивать к своему приложению.

- Go to the telegram bot - https://t.me/myapi_aibot , click start - registration is completed, we take accesses and some test amount on the balance, read the instructions and you can already contact through the postman or write an application, fasten it to your application.



## Features that may be of interest:

- Сама API работает в другой стране по понятным причинам. То есть, если вы не в Иране, Ираке или РФ - вам не нужну это.

- The API itself works in another country for obvious reasons. That is, if you are not in Iran, Iraq or the Russian Federation, you do not need it.

- Трафик не будет шифроваться, так как API работает без домена по http. При удачном стечении обстоятельств и расширении проекта, куплю домен .com и подключу SSL по https шифрование. А пока что так.

- The traffic will not be encrypted, since the API works without a domain over http. With a successful combination of circumstances and the expansion of the project, I will buy a .com domain and connect SSL over https encryption. For now, that's it.

- Я оставляю за собой право удалять выделенные мною же средства для проверки, спустя срок от недели без объяснения причин. Так же оставляю за собой право на удаление данных, при отсутствия активности больше 2 недель.

- I reserve the right to delete the funds allocated by me for verification, after a period of at least a week without explaining the reasons. I also reserve the right to delete data if I have been inactive for more than 2 weeks.

- Генерится один ключ для пользователя, он может использовать его для разных приложений. Конечно в идеале, создавать отдельные ключи для разных приложений. Но пока что я остановился на простом варианте, так как не уверен, что API будет популярна. Пока я рассчитываю только на свои проекты. Не вижу смысла городить огород на проекте для личных нужд, пойдет - доработаем. Сейчас цель - надежно, чисто и просто.

- One key is generated for the user, he can use it for different applications. Of course, ideally, create separate keys for different applications. But for now, I've settled on the simple option, since I'm not sure that the API will be popular. So far, I'm counting only on my projects. I don't see any point in planting a vegetable garden on a project for personal needs, if it goes, we'll finalize it. Now the goal is reliable, clean and simple.

- API работает на асинхронном коде и должна выдерживать нагрузки. К сожалению, аккаунт Open AI не поддерживает асинхронную загрузку одиночных файлов, вот жалость или наглость, шутка. API тестовая, а потому, прошу с пониманием отнестись к возможным проблемам или недоработкам. Принимаю предложения.

- The API runs on asynchronous code and must withstand loads. Unfortunately, the Open AI account does not support asynchronous downloading of single files, that's a pity or an impudence, a joke. The API is a test one, and therefore, I ask you to understand possible problems or flaws. I accept offers.

Хорошего настроения и удачных разработок!
Good mood and successful developments!
