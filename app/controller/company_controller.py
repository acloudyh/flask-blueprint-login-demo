# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : company_controller.py
# Software: PyCharm
# Time    : 2020/3/20 10:12
# Description:

from flask import Blueprint, current_app, render_template, request, redirect, url_for
from flask_login import login_required

from app import db
from app.models.company_model import Company
from app.service.company_service import get_all_company

company = Blueprint('company', __name__)


@company.route("/companys", methods=['GET'])
@login_required
def companys():
    current_app.logger.info('获取所有信息')
    companys = get_all_company()
    return render_template('company/index.html', companys=companys)


@company.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('company/create.html')
    elif request.method == 'POST':
        company = Company()
        # company.name = request.get_json().get("name")
        # company.age = request.get_json().get("age")
        # company.address = request.get_json().get("address")

        company.name = str(request.form['name'])
        company.age = str(request.form['age'])
        company.address = str(request.form['address'])
        db.session.add(company)
        db.session.commit()
        current_app.logger.info('创建成功%s', company.to_json())
        return redirect(url_for('company.companys'))


@company.route("/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    if request.method == 'GET':
        company = Company.query.get(id)
        return render_template('company/update.html', company=company)
    else:
        company = Company.query.get(str(request.form['id']))
        company.name = str(request.form['name'])
        company.age = str(request.form['age'])
        company.address = str(request.form['address'])
        db.session.commit()
        return redirect(url_for('company.companys'))


@company.route("/delete/<int:id>", methods=['GET', 'DELETE'])
@login_required
def delete(id):
    company = Company.query.get(id)
    db.session.delete(company)
    db.session.commit()
    current_app.logger.info('删除成功name:[%s],id:[%s]', company.name, id)
    return redirect(url_for('company.companys'))
