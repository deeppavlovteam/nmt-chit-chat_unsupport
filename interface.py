from nmt import interface
interface.init('/home/kuznetsov/qa_dialog/eah')
print(interface.send('Здравствуйте , Подскажите , веду бух учёт на Эльбе . Контур . Сохранил платёжные поручения для уплаты страховых платежей , сохранил их в текстовом формате  ( так сохраняет сама программа ), а в банк не могу импортировать . пишет , что в файле нет необходимых реквизитов , хотя года открываешь текстовый файл вся информация присутствует . Спасибо .'))
