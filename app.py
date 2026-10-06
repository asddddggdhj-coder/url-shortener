from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import string
import random

app = Flask(__name__)

# إنشاء قاعدة البيانات والجداول عند التشغيل
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            api_key TEXT UNIQUE NOT NULL,
            tier TEXT DEFAULT 'free',
            usage_count INTEGER DEFAULT 0,
            limit_count INTEGER DEFAULT 100
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE NOT NULL,
            original_url TEXT NOT NULL,
            api_key TEXT NOT NULL,
            clicks INTEGER DEFAULT 0,
            FOREIGN KEY (api_key) REFERENCES users (api_
