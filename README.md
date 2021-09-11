# Class 32 - Permissions & Postgresql

*Author*: Kassie Bradshaw

[Link to my Repo](https://github.com/kassiebradshaw/drf-api-permissions-postgres)

## Overview

Let's move our site closer to production grade by adding Permissions and Postgresql Database.

## Feature Tasks & Requirements

* You have been supplied with two demos, each presenting a new key feature
  * `blogapi-permissions` demonstrates how to restrict access to portions of your API's data
  * `blogapi-postgres` demonstrates switching over to using postgres vs sqlite

* Your job is to merge the functionality of both demos.
* Customize your project to use different application features/models than `Blog` and `Post`

## Features - Django REST Framework

* [x] Make your site a DRF powered API as you did in previous lab
* [x] Adjust project's permissions so that only authenticated users have access to API
* [x] Add a custom permission so that only author of blog post can update or delete it.
* [x] Add ability to switch user's directly from browsable API.

## Features - Docker

* [x] **NOTE** - Refer to demo for built out `Dockerfile` and `docker-compose.yml` examples
* [x] Create Dockerfile based off `python:3.8-slim`
* [x] Create `docker-compose.yml` to run Django app as a web service.
* [x] Enter `docker-compose up --build` to start your site.
* [x] Add `postgres 11` as a service
  * **NOTE** - it is not required to include a volume so that data can persist when container is shut down.
* [x] Go to browsable api and confirm site properly restricts users based on their permissions.

## Stretch Goals

* [ ] Try different permission levels, including custom ones.
* [ ] Figure out how to directly access postgres running inside container.
  * Hint: it will take research
* [ ] Add a `volume` to persist data when container is shut down.
