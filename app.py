from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blocks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель блока
class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    block_type = db.Column(db.String(50))  # 'links', 'transitions', etc.
    name = db.Column(db.String(255))
    url = db.Column(db.String(255))
    icon = db.Column(db.String(255), nullable=True)  # для иконки

# Виртуальные машины (остаются статическими)
virtual_machines = {
    'sh0': 'https://10.25.1.18:8006',
    'sh1': 'https://10.25.1.32:8006',
    'sh2': 'https://10.25.1.37:8006',
    'sh3': 'https://10.25.1.31:8006',
    'sh4': 'https://10.25.1.33:8006'
}

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    # Загружаем блоки по типам
    blocks_data = {}
    for block_type in ['links', 'transitions']:
        blocks_data[block_type] = Block.query.filter_by(block_type=block_type).all()
    return render_template('index.html', virtuals=virtual_machines, blocks=blocks_data)

# API для получения всех блоков (для AJAX)
@app.route('/api/blocks/<block_type>')
def get_blocks(block_type):
    blocks_list = Block.query.filter_by(block_type=block_type).all()
    return jsonify([{'id': b.id, 'name': b.name, 'url': b.url, 'icon': b.icon} for b in blocks_list])

# API для добавления блока
@app.route('/api/blocks/<block_type>/add', methods=['POST'])
def add_block(block_type):
    data = request.json
    new_block = Block(
        block_type=block_type,
        name=data['name'],
        url=data['url'],
        icon=data.get('icon')
    )
    db.session.add(new_block)
    db.session.commit()
    return jsonify({'status':'success', 'id': new_block.id})

# API для редактирования блока
@app.route('/api/blocks/<int:block_id>/edit', methods=['POST'])
def edit_block(block_id):
    data = request.json
    block = Block.query.get_or_404(block_id)
    block.name = data['name']
    block.url = data['url']
    if 'icon' in data:
        block.icon = data['icon']
    db.session.commit()
    return jsonify({'status':'success'})

# API для удаления блока
@app.route('/api/blocks/<int:block_id>/delete', methods=['POST'])
def delete_block(block_id):
    block = Block.query.get_or_404(block_id)
    db.session.delete(block)
    db.session.commit()
    return jsonify({'status':'success'})

# Страница админки
@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)