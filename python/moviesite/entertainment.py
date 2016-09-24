#! /usr/bin/python
# encoding: utf-8

import media
import fresh_tomatoes

liga_da_justica = media.Movie('A Liga da Justica', 'Grupo de super herois que lutam contra viloes', 'https://s-media-cache-ak0.pinimg.com/564x/1e/32/22/1e322211b027a98a69510ed72a97cd31.jpg', 'https://www.youtube.com/watch?v=fIHH5-HVS9o')
passageiros = media.Movie('Passageiros', 'Uma viagem emocionante ao espaço com descobertas incriveis', 'http://cdn.traileraddict.com/content/columbia-pictures/passengers-5.jpg','https://www.youtube.com/watch?v=yVXQq2u6OP0')
wonder_woman = media.Movie('Mulher Maravilha', 'Deusa grega que leva um aviador de volta pra casa','https://s-media-cache-ak0.pinimg.com/564x/f3/e4/73/f3e47329b4a2ffd351c0f6026d97c140.jpg','https://www.youtube.com/watch?v=Tgk_63b-Mrw')

movies = [liga_da_justica, passageiros, wonder_woman]
fresh_tomatoes.open_movies_page(movies)