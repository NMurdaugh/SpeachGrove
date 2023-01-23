# SpeachGrove


## Overview

This app will allow a user to select a speaker and generate a speech in that speaker's voice given prompts by the user, e.g.:

- Selected Speaker: Robert Deniro
- What would you like Mr. Deniro to do for you? "Please give my father, James Long, a birthday message. He turns 58 this year. His favorite movie is Meet the Parents. Make it funny and endearing."


### Utilizations

- OpenAi's ChatGPT DaVinci model via either OpenAi's native API or the open-source Chronology library
- FakeYou via the fakeyou.py open-source library.


## Features


### Essential

- Allow user to pick a speech writer and describe the speech they want
- Establish small selection of tested speech writers
- Establish user profiles
- Store all data for users, allow to be accessed later
- Allow user to download products
- Provide built-in sharing
- Manage FakeYou audio length restrictions effectively


### Secondary

- Integrate OpenAI's moderation suite to ensure safe and appropriate use of app
- Test and add more speech writers
- Allow past prompts to be used to generate new ones
- Provide automatic wav splicing for extending a prior speech


### Long-Term

- Make sharing more robust; use OAuth for social media sharing
- Establish free options and paid options; could be package based, as-a-service, or combination
- Integrate reCaptcha or similar to prevent overload
- Greet user upon login with a personalized message that references their last use case, ie: "Welcome back, ALex, did your dad enjoy his birthday greeting?"
- Format app to microservices
- Ever expand available speech writers


## Data Model


### User

- username
- password
- email
- first name
- last name
- permissions

**Later**

- paid status


### Request

- datetime
- id
- associated user
- associated response
- speaker
- speaker token
- user request text
- complete request text

**Later**

- original request ID (if applicable)
- flagged: boulean


### ChatResponse

- datetime
- ID
- associated user
- tokens used
- associated request
- associated audio response
- response text

**Later**

- AI generated summary of request


### AudioResponse

- datetime
- ID
- associated user
- associated request
- associated ChatResponse
- audio file

**Later**

-original audio


## Schedule


### 27Jan23 (T-19)

Successful use of OpenAI and Fakeyou to generate a request and return an AI generated speech in the selected speaker's voice

- All models established
- Necessary core libraries integrated
- Basic web page for input and response
- One or two test writers available


### 01Feb23 (T-14)

Users will see a more robust webpage, will be able to share audio and access old audio

- Models will be tested
- Create user history page where they can check out old projects
- Vue and CSS framework (likely Tailwind) in use


### 03Feb23 (T-12)

User will have a smoother experience that is capable of filtering unsafe or inappropriate content before a composition is attempted.

- Integrate the OpenAI moderation system; tune the filter following testing


### 08Feb23 (T-7)

User will be able to extend past speeches

- pass stored Chat response back to Chat asking it to expand on its previous product
- splice new speech segment wav onto the back of the previous


### 14Feb23 (T-1)

User will have a more aesthetic and streamlined experience

- Integrate UX/UI design and use flow
- **Deployment**


### 15Feb23 (T)

**PRESENTATION**


### 22Feb23 (T+7)

User will be able to share to social media sites directly

- Integrate OAuth


### TBD