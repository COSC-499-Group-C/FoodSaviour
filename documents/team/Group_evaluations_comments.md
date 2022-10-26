### Group Evaluations and comments

- How is user authentication handled, is there already a backend service available?

  - We are planning to use Django which provides a level of security when it comes to passwords. It has a built-in set of password validators, some of which are enabled by default in new projects. If required by the the client we plan to use further measures like OAuth2

- Are you preventing website administrators from viewing health information?

  - That’s correct we plan to keep the health information only visible to Health Professionals if provided with consent by the user
- How do you plan to implement the discussion board? Will it be monitored manually?

  - We are planning to have a small community board which will have basic functionality to post comments. We haven’t dug into the logistics of how it will be monitored just yet, the client will decide in future if moderators will be required for the board

- What system will you use to prevent spam and other malicious uses of the system?
  - The website will be used initially by a close-knit community so we are not prioritizing spam users. We are still in discussion of any other security measures client will like to have but nothing is concrete just yet.

- Will all functions be available on mobile devices? How do you plan to adapt the dashboard for mobile?

  - Yes, we will make sure the site is dynamic and compatible with desktop and mobile. We plan to use grids and bootstrap to make it as compatible as possible but we don’t plan to have a separate web app just for mobile or handheld devices 

- Will the discussion board be moderated?
  - It will be moderated by admins/professionals (ability to delete messages).

- Should your DFD differentiate between the different types of users?
  - They do, the legend shows the different colours that identify the different users.

- What about users that fall under multiple groups? Will they need to manage multiple accounts or can they switch between profiles?
  - Account is a hierarchy system, if the user is a basic leisure user and professional, a professional account will cover all functionality. We could assign multiple role types to a single account too.

- You could’ve gone into more detail comparing the options who had for the tech stack?
  -  Unfortunately our client required us to use Django CMS from the starting of the project. Although we proposed FastApi and flask but they were eventually scrapped off because of scalability issues.
- In your milestones report, it was mentioned in the last milestone that users can make donations. How do you plan to implement this so that it is secure? Could you also define what would be considered in a “timely manner”?
  - Donations are an optional requirement, so this is to be determined.
- In the requirements, it was mentioned that users will have to log in to access different features based on their roles. How do the users get assigned a role? Will the administrators have to manually assign them?
  - Admins will most likely assign roles. The amount of new users won’t be too many, so it is a manageable task by an admin.
- The information presented was well-organized and easy to follow.
  - Thanks.
- You’ve mentioned both users with or without accounts will be able to have access to the website. Will features of the website be limited for users without accounts? 
  - Yes, without an account you will not have access to any of the Health and Wellness trackers, progress graphs, or weekly challenges.
- Your presentation seemed to not include the testing part of your project. Will there be any testing done and if so which testing strategies/tools will be used?
  - We will most likely have basic unit testing in python, and then testing plans in Excel spreadsheet, as well as manual testing on the website and database throughout development.
- What is the budget? Security is an important issue; how will you maintain privacy while minimizing costs?
  - The site will be low budget since it is meant for non-profits with minimal funding.
- How will you handle event cancellation?
  - Most likely weekly challenges will be halted, and events will be removed from the TA calendar. Trackers and individual graphs should still function, and professionals should still be able to view patient progress and give feedback.
- Can the maintainability be measured? It would be great if this is elaborated.
  - Unfortunately, there is not a big team which will be supporting the project after it is launched so measuring maintainability is slightly difficult for us. We currently hoping to have a project which is scalable enough for future developers to work on.
- Prototype as the last milestone doesn’t sound like a good idea. Having user feedback throughout the developing phase is important.
  - Thank you for your input. We will take that into consideration.
- What are the client expectations on front ends? Do they want something dynamic or static?
  - The website will be dynamic. Each user will see different graphs and feedback, and graphs will update as trackers are filled.
- What will the individual tracker track? What kind of results will be displayed for the particular individual’s dashboard
  - Trackers will track multiple health and wellness measures that are input by the user, and visualizations of input data will be displayed in the dashboard as well as goal progress and professional feedback.
- Will you be integrating your testing into your github repository ?
  - We may have continuous integration with Github Actions.
- What features will be available on the map of the Okanagan Rail Trail
  - Able to see important location along the trail and other trails connecting the rail trail
- Look into Open Street Maps, which allows access to maps without needing to use a google maps API!
  - We will look into this, thank you.
- Also take a look at Mapbox!
  - Okay.
- What approach will you take for ensuring long term maintainability
  - We hope to have a highly scalable web app since there is no large active group maintaining it after the Capstone is done. Aim is to have it set up with the current requirements and make it easy for any future developers to expand
- Will patients be able to make “friends” and compare some statistics for the challenges and events?
  - All the users will be able to see other statistics from challenges and events through graphs and other trackers
- How will you verify that a health professional is indeed a health professional, and it’s not just Joe Schmoe creating a health professional account?
  - The admins will most likely manually assign roles to each registered account so that there are no false professionals or trail ambassadors and no Joe Schmoes.
