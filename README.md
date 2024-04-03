# Seal project 4

# Product Requirements Documentation

- **Developer: Yuliya Buiko**
- **App Name: Hospital Management System**
- **Description: Full-stack web application to handle a hospital’s work. The system should have an interface for creating doctors' accounts, inserting and updating patients and adding records for all patients’ details, and it should also offer a method for quickly accessing and searching records.**
- **GitHub Url Back End:https://github.com/uliaarkadz/BE_PROJECT4.git**
- **GitHub Url Front End:https://github.com/uliaarkadz/FE_PROJECT4.git**
- **Deployed WebSite FE:**
- **Deployed WebSite BE:**

## User Stories

- Users should be able to see the site on desktop and mobile
- Users can create a new doctor
- Users can create a new patient
- Users can see a list of all the patents
- Users can assign doctors and change patient statuses
- Users can update patient
- Users can delete patient
- Users can add patient visit information

## List of Dependencies

## Route Map

List of different routes and their purpose in the app

|   Endpoint   | Metod  |           Response           | Other |
| :----------: | :----: | :--------------------------: | :---: |
|   /doctor    |  GET   |    Return all the doctors    |       |
|   /doctor    |  POST  |      Create new doctor       |       |
| /doctor/:id  |  GET   | Return doctor records by id  |       |
| /doctor/:id  |  PUT   |     Update Doctor by id      |       |
| /doctor/:id  | DELETE |  Delete doctor record by id  |       |
|   /patient   |  GET   |   Return all the patients    |       |
|   /patient   |  POST  |      Create new patient      |       |
| /patient/:id |  GET   | Return patient records by id |       |
| /patient/:id |  PUT   |     Update patient by id     |       |
| /patient/:id | DELETE | Delete patient record by id  |       |

## ERD (Entity Relationship Diagram)

![Entity Relationship Diagram](/hospitalmanagement/images/image.png)
