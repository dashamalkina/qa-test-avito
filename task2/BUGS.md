1) ФП: Айтем можно создать без `name`. ОП: Айтем нельзя создать без `name`.
2) ФП: Айтем можно создать без `price`. ОП: Айтем нельзя создать без `price`.
3) ФП: Айтем можно создать без `sellerId`. ОП: Айтем нельзя создать без `sellerId`.
4) ФП: Айтем можно создать c любым значением `price`. ОП: `price` айтема должен был неотрицательным числом.
5) ФП: При создании айтема в поле `name` записывается значение "dsdsd". ОП: При создании айтема в поле `name` записывается значение переданное значение.
6) ФП: При запросе всех айтемов по `sellerID` поля `name` и `id` перепутаны местами. ОП: При запросе всех айтемов по `sellerID` поля `name` и `id` корректные.
7) ФП: При запросе всех айтемов по не существующему `sellerID` получаем ответ 200 и пустой массив айтемов. ОП: При запросе всех айтемов по не существующему `sellerID` получаем ответ 400, так как такого селлера нет.
8) ФП: При запросе статистики по `id` айтема, поле `viewCount` на 2 больше чем при создании. ОП: (возможно не баг) При запросе статистики по `id` айтема, поле `viewCount` такое же как при создании айтема.
