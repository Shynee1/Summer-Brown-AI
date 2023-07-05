servesAll(american, [salad, steak, sandwiches, burgers, fried_chicken]).
servesAll(burger_place, [burgers, fries, onion_rings]).
servesAll(chinese, [eggrolls, rice, shrimp, soup, noodles]).
servesAll(indian, [papadam, bagan_bharta, rice, tandoori, naan]).
servesAll(italian, [salad, pasta, cioppino, snapper, bread, garlic_bread]).
servesAll(japenese, [sashimi, rice, tempura, noodles]).
servesAll(mediterranean, [gyros, hummus, pita, falafel]).
servesAll(mexican, [tacos, beans, rice, enchiladas, fish_tacos]).
servesAll(pizza_place, [pizza, salad, garlic_bread]).
servesAll(thai, [rice, noodles, larb, pad_thai]).

serves(Kind, Dish):- 
    servesAll(Kind, Dishes), 
    member(Dish, Dishes).

allDishes(vegetarian, [beans, bagan_bharta, enchiladas, falafel, hummus, pizza, salad, soup, tempura, onion_rings, naan, papadam, bread, rice, noodles, pita, garlic_bread, pasta, fries]).
allDishes(meat, [burgers, enchiladas, gyros, pad_thai, pizza, steak, swiches, fried_chicken, tacos, toori, larb]).
allDishes(seafood, [snapper, cioppino, sashimi, shrimp, clams, fish_tacos, tempura]).
allDishes(starch, [naan, papadam, bread, rice, noodles, pita, garlic_bread, pasta, fries]).

dish(Type, Dish):-
    allDishes(Type, Dishes),
    member(Dish, Dishes).

location(yans, thayer_street).
location(pizza_marvin, fox_point).
location(bajas, thayer_street).
location(andreas, thayer_street).
location(chinatown, thayer_street).
location(kabob_n_curry, thayer_street).
location(waterman_grille, wayland).
location(dolores, fox_point).
location(tallulahs, fox_point).
location(red_stripe, wayland).
location(pasta_beach, wayland).
location(haruki, wayland).
location(heng, thayer_street).
location(mikes, thayer_street).
location(east_side_pocokets, thayer_street).
location(bees, fox_point).
location(shake_shack, thayer_street).
location(al_forno, fox_point).
location(lims, wayland).

cuisine(yans, chinese).
cuisine(pizza_marvin, pizza_place).
cuisine(bajas, mexican).
cuisine(andreas, mediterranean).
cuisine(chinatown, chinese).
cuisine(kabob_n_curry, indian).
cuisine(waterman_grille, american).
cuisine(dolores, mexican).
cuisine(tallulahs, mexican).
cuisine(red_stripe, american).
cuisine(pasta_beach, italian).
cuisine(haruki, japenese).
cuisine(heng, thai).
cuisine(mikes, pizza_place).
cuisine(east_side_pocokets, mediterranean).
cuisine(bees, thai).
cuisine(shake_shack, burger_place).
cuisine(al_forno, italian).
cuisine(lims, thai).

restaurant(Restaurant, Dish, Location) :-
    location(Restaurant, Location),
    cuisine(Restaurant, Cuisine),
    serves(Cuisine, Food),
    dish(Dish, Food).


/* 
1. location(X, wayland).
2. cuisine(X, italian).
3. serves(X, snapper).
4. serves(X, rice).
5. restaurant(X, vegetarian, fox_point).
*/

