# index.py
from flask import Blueprint, request, send_file, render_template
import os
import logging

index_bp = Blueprint('index', __name__)

@index_bp.route('')
def index():
  logging.info('asdas')
  return render_template("index.html")