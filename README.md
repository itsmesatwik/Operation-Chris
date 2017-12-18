# Operation Chris

Our project is a web app that takes in food order and display them in the kitchen.
Here is a link to our app runing on heruko: http://hendrickhousedining.herokuapp.com

## Homepage

This is homepage where you can login with UIUC email and Hendrick House meal number.

![Alt text](https://raw.githubusercontent.com/susielau/Operation-Chris/master/sreenshots/Homepage.png)

Currently the email and meal numbers in our database are made up. We will connect to Hendrick House database later.

To protect user information, the password in our database are hashed.

When you try to login with invalid credentials or jump to order page, you will be redirect back to login page.

![Alt text](https://raw.githubusercontent.com/susielau/Operation-Chris/master/sreenshots/Invalid_Credentials.png)

## Order Page

Here is the order page
You can log out at the bottom of the page if you want.

![Alt text](https://raw.githubusercontent.com/susielau/Operation-Chris/master/sreenshots/Order_Page.png)

We have two different kinds of items on menu currently. When clicking on the item, a corresponding window will show up.
You can customize your order here.

![Alt text](https://raw.githubusercontent.com/susielau/Operation-Chris/master/sreenshots/Chicken_Customize.png)

After choosing the desired options, you can click the "Place Order" button to place the order.
It will redirect you to the success page if the order is successfully placaed.

## Success Page

This is the order success page. You can log out or close the window if you want.

![Alt text](https://raw.githubusercontent.com/susielau/Operation-Chris/master/sreenshots/Success.png)

## Kitchen Page

Here is the kitchen page, which is used in kitchen to see all the orders and make them accordingly.

![Alt text](https://raw.githubusercontent.com/susielau/Operation-Chris/master/sreenshots/Kitchen1.png)

When a order is done, you can click the "Done" button on the right side of the order to remove it from the list.

![Alt text](https://raw.githubusercontent.com/susielau/Operation-Chris/master/sreenshots/Kitchen2.png)
Here a order is removed

## Improvement

We will keep working on the project and talk to Hendrick House to see whether they'll use it.
There are a lot of things we can imporve:
 * Put more items on the menu.
 * Notify customers when the order is done
 * Make sure the order is placed during a meal
 * Coordinate with the meal number system of Hendrick House


## Built With

* [Flask](http://flask.pocoo.org) - The web framework used
* [PostgreSQL](https://www.postgresql.org) - The databse used


## Authors

* **Susie Liu** - *Back-end* - [susielau](https://github.com/susielau)
* **Jenny Chen** - *Front-end* - [Xiangmingchen](https://github.com/Xiangmingchen)

## Acknowledgments

* flat icon for the falling food objects on homepage
* font awesome for icons
