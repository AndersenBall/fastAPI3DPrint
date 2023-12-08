# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:08:40 2023

@author: andersen, michael
"""

import uvicorn 


if __name__ == "__main__":
    uvicorn.run("app.app:app",port=8000,reload=True)