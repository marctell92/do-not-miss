# DoNotMiss

![alt](readme-images/am-i-responsive.JPG)

[Visit site here](https://do-not-miss.herokuapp.com/)


This website offers basic information about the main EDM festivals around the globe such as the location, dates and artists. It aims to be a guide to all Electronic Dance Music fans who are in search of the main events in the world.
This website is mobile-first design and it's fully responsive and accessible on a vast range of devices, making it easy to navigate for all kinds of users.
 
## User Experience (UX)

### Strategy Plane
#### Target audience for EDMfestivalsEU:

- Users aged 16-40, given the fact that Electronic Dance Music is more extensive between this age range.
- Users interested in Electronic Dance Music.
- Users interested in music events, specially big festivals.
- Users interested in planning their vacation or weekend getaway around a music festival in Europe.
- Users interested in finding information about an specific festival.


#### Business Goals

Allow users to find the best EDM festivals in Europe.
Present the website on a user-friendly form, where information can be absorbed easily.
Help the user understand the information displayed within the first visit to the website.
Allow users to add any festivals to the database.
Allow admin to edit and delete information from the database.

#### User stories 
- ##### As a First Time Visitor, I want to...
    - Easily understand the content in order to find the information I'm looking for.
    - Easily navigate and find content through the website in an user-friendly way.
    - Find visual resources that support and complement the content.

- ##### As a Returning Visitor, I want to...
    - Find the familiar interface and layout which I already experienced.

#### Features consideration

We've used the below table to consider which features was worth adding, considering their
importance and the viability of implementing them. The ones highlighted in red were left on the side 
to be considered in the future.

![alt](readme-images/features.JPG)

### Scope Plane

Minimal Viable Product for this project is a website with at least the below features;

- Navigation Bar on desktop and tablet screen, hamburger on mobile.
- Social Media Links
- Interactivity unfolding the list of festivals for each country.
- Ability to perform CRUD in the database.

### Structure Plane
- The user can navigate through the different sections of the page
using a navigation bar on desktop and tablet screen versions.
- The user can navigate through the different sections of the page
using a hamburger on mobile screen versions.

### Skeleton Plane
- Mobile Screen
    - ![alt](wireframes/ms2.edmfestivalseu.mobile.png)
- Tablet Screen
    - ![alt](wireframes/ms2.edmfestivalseu.tablet.png)
- Desktop Screen
    - ![alt](wireframes/ms2.edmfestivalseu.desktop.png)

### Surface Plane
This website aims to give a festival lights feeling.
Creative design has been applied in order to adapt to this look and feel.
 
- Colors: #4e1f32, #e78ba8, #dedede
- Fonts: Chakra Petch and Bai Jamjuree
- Images
    - The Hero image aims to set the color palette of the website and give a festival crowd feeling.
    - Country images aim to allow the user to identify hich country is going to be selected.
    - Festival images aim to reflect the ambience on each festival.

    ## Features
### Existing Features
- Responsive on all devices: allows the user to navigate comfortably on the page regardless of the device type used.
- Navigation Bar and hamburger: allows the user to navigate through the web sections and pages with ease.
- Add, edit and delete buttons, as well as search tab, allows user to perform CRUD actions
- Footer: allows users to access the different social media channels of DoNotMiss.


## Technologies Used
### Languages
- HTML5
- CSS3
- Javascript
- Python
- MongoDB

### Frameworks, Libraries & Programs Used
- [Github](https://github.com/): used to store the projects code.
- [Gitpod](https://gitpod.io/workspaces): used for version control.
- [Materialize 1.0.0](https://materializecss.com/about.html): used to assist with the responsiveness and styling of the website.
- [Balsamiq](https://balsamiq.com/): used for wireframe design.
- [jQuery v3.5.1](https://jquery.com/): used to implement interactivity on the page.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/): used for the development of the app.


## Testing
### W3C Markup Validator and W3C CSS Validator
- W3C Markup Validator
    - ![alt](readme-images/w3c-markup-validator.JPG)
- W3C CSS Validator
    - ![alt](readme-images/w3c-css-validator.JPG)
- Jshint JavaScript Validator
    - ![alt](readme-images/maps-js-validator.JPG)
    - ![alt](readme-images/script-js-validation.JPG)
    - ![alt](readme-images/email-js-validation.JPG)


### Lighthouse Chrome Developer Tools
![alt](readme-images/lighthouse.JPG)

### Testing User Stories
##### As a First Time Visitor, I want to...
- Easily understand the content in order to find the information I'm looking for.
    - Webpage is well structured and sections are presented clearly to the user.
![alt](readme-images/hero-header.JPG)
![alt](readme-images/countries-section.JPG)
![alt](readme-images/footer.JPG)
- Easily navigate and find content through the website in an user-friendly way.
    - Navigation bar allows user to move through different sections of the website.
![alt](readme-images/nav-bar.JPG)
- Find visual resources that support and complement the content.
    - Images are displayed to support text.
![alt](readme-images/festival-card.JPG)
- Have the possibility to get in touch with EDMfestivalsEU and have access to their Social Media links.
    - Get in touch page accessible from navigation bar.
![alt](readme-images/nav-bar.JPG)

##### As a Returning Visitor, I want to...
- Find the familiar interface and layout which I already experienced.
    - Layout is easy to understand, user friendly and intuitive.

### Further testing
- The Website has been tested in all different screen devices from Google Developer Tools.
- The Website has been viewed on a variety of devices and screen sizes.
- The Website has been tested on Google Chrome, Internet Explorer, Safari and Microsoft Edge.
- All links have been tested
- All locations on Maps have been tested.
- Interactivity has been tested.
- EmailJS functionality has been tested.

### Fixed bugs
Many bugs were encountered on the way. The majority of them were fixed with the help of the Slack Code Institute community and Stack Overflow community. Some of the most challenging bugs were:
- On mobile screen, hamburger icon expands when clicked, but will not go to its original state when clicked again: fixed by removing doubled bootstrap.js script.
- Images making the page overflow on small screen devices: fixed structure of divs and apply position attributes with the help of Google Developer Tools.

## Deployment
### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/marctell92/boundless)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://marctell92.github.io/boundless/) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/marctell92/boundless)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/marctell92/boundless)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/marctell92/boundless
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/marctell92/boundless
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

## Credits
- All code has strong inspiration from all learning material given by Code Institute.
- Multiple pieces of code have been taken from Bootstrap Library and modified to fit the design needs.

### Content
- README.md was strongly inspired by the Sample README from user lechien73 on GitHub, sample given by the Code Institute Mentor Team.
- Deployment section of the README.md was copied from the above mentioned Sample README.

### Media
- All images were obtained via Google Images, using the Usage Rights tools to make sure all of them had Creative Commons licenses.

### Acknowledgements
- Code Institue Tutor Support and Mentor Team. 