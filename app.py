from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Виртуальные машины (можно расширять)
virtual_machines = {
    'sh0': 'https://10.25.1.18:8006',
    'sh1': 'https://10.25.1.32:8006',
    'sh2': 'https://10.25.1.37:8006',
    'sh3': 'https://10.25.1.31:8006',
    'sh4': 'https://10.25.1.33:8006'
}
@app.route('/admin.html')
def admin():
    return render_template('admin.html')
# Блоки для админки (можно расширять)
blocks = {
    'links': [
        {'name': 'Админка внутреннего сайта', 'url': 'https://is.city.tambov.gov.ru:8055'},
        {'name': 'Админка внешнего сайта', 'url': 'https://city.tambov.gov.ru/typo3'},
        {'name': 'Система тестирования', 'url': 'http://10.25.1.55'},
        {'name': 'Система планирования', 'url': 'http://task.city.tambov.gov.ru'},
        {'name': 'ПОС', 'url': 'https://pos.gususlugi.ru/admin'},
        {'name': 'Почта', 'url': 'https://webmail.tambov.gov.ru/postfixadmin'}
    ],
    'transitions': [
        {'name': 'На внутренний сайт', 'url': 'http://10.25.1.2'},
        {'name': 'На внешний сайт', 'url': 'https://city.tambov.gov.ru'},
        {'name': 'Телефонный справочник администрации города', 'url': 'http://app4.tambov.gov.ru/tmbphones'},
        {'name': 'Телефонный справочник области', 'url': 'http://phones.tambov.gov.ru'}
    ],
    # Можно добавлять новые блоки через API или интерфейс
}

@app.route('/')
def index():
    return render_template('index.html', virtuals=virtual_machines, blocks=blocks)

@app.route('/launch_vm/<vm_id>', methods=['POST'])
def launch_vm(vm_id):
    if vm_id in virtual_machines:
        # Тут должна быть логика запуска VM через API гипервизора
        # Для примера просто возвращаем сообщение
        return jsonify({'status':'success', 'message': f'Виртуальная машина {vm_id} запущена'})
    else:
        return jsonify({'status':'error', 'message':'Виртуальная машина не найдена'}), 404

if __name__ == '__main__':
    app.run(debug=True)