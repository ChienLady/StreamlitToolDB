import streamlit as st
from streamlit_elements import elements, mui, html, lazy, sync
import json

DEFAULT_COLUMNS = [
    # id
    {'field': 'id',
     'headerName': 'ID',
     'flex': 0.1,
     'description': 'document id'},
    # source
    {'field': 'source',
     'headerName': 'Source',
     'flex': 0.2,
     'editable': True,
     'description': 'Document source: url/file'},
    # content
    {'field': 'content',
     'headerName': 'Content',
     'flex': 0.6,
     'editable': True,
     'description': 'Document content'},
    # has_embedding
    {'field': 'has_embedding',
     'headerName': 'Embedding',
     'type': 'boolean',
     'flex': 0.1,
     'description': 'This document has embedding: True/False'}
]
DEFAULT_ROWS = [
    {'id': 'a'*15, 'source': 'https://discuss.streamlit.io/', 'content': 'Jon', 'has_embedding': True},
    {'id': 'b'*15, 'source': 'https://discuss.streamlit.io/t/streamlit-elements-build-draggable-and-resizable-dashboards-with-material-ui-nivo-charts-and-more/24616/44', 'content': 'Cersei', 'has_embedding': False},
]

def main():
    with elements('documents'):
        with mui.Paper(key='temp',
                       sx={'display': 'flex',
                           'flexDirection': 'column',
                           'borderRadius': 3,
                           'overflow': 'hidden'
                           },
                       elevation=1):
            with mui.Box(sx={'flex': 1, 'minHeight': 0}):
                mui.DataGrid(
                    columns=DEFAULT_COLUMNS,
                    rows=DEFAULT_ROWS,
                    autoHeight=True,
                    disableColumnFilter=False,
                    slots = {'toolbar': mui.GridToolbar()},
                    pageSize=10,
                    rowsPerPageOptions=[10],
                    checkboxSelection=True,
                    density='standard',
                    disableSelectionOnClick=False
                )   
