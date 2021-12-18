# Search Property

This is a microservice that allows all types of users to be consulted for properties information.

## Brief

- The statuses "pre_sale", "sale" and "sold" can be used to examine the attributes (properties with different states should never be visible to the user).
- These properties can be filtered by year of construction, city, and state.
- On the same query, users can apply numerous filters.
- The following property information is available to users: Address, City, Status, Sale Price, and Description.

## Project Architecture

It was used wsgiref (Utilities and Reference Implementation) for the implementation and docker for build the develop/deploy enviroment.

The project is based on Domain Driven Design (DDD), but with a few exceptions.

- The _infraestrure_ layer has been renamed to **data** layer.
- The _application_ layer has been renamed to **deal** layer.
- The _domain_ layer hasn't been renamed.

The information flow starts in the _data layer_ and continues via the _deal layer_, the _domain layer_ contains the application's core logic.
