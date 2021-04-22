import pytest
import requests

passed = 'Passed'
failed = 'Failed'

def logs(test, status, error='Not errors'):
    with open('tests.log', 'a+', encoding='utf-8') as f1:
        line=f'{test}, {status}, {error}\n'
        f1.writelines(line)


def test_only():
    test = test_only.__name__
    req = requests.get('http://127.0.0.1:8080/api/pornostars')
    if req.text == "All actors: {'Jonny Sins': {'id': '001', 'username': 'Jonny_Big_Dick_28', 'email': 'jonnysinsvkisku28@porn.cum', 'department': 'Anal Department', 'date_joined': '13.01.2004'}, 'Sasha Grey': {'id': '002', 'username': 'Sasha_Grey_House', 'email': 'sashagreyhouse13@porn.cum', 'department': 'Cook Cum Pie', 'date_joined': '15.06.2001'}, 'Ariana Marie': {'id': '003', 'username': 'Anna_Maria_000', 'email': 'arianafishmaster000@porn.cum', 'department': 'Ass Accept', 'date_joined': '27.02.2005'}}":
        logs(test, passed)
    else:
        logs(test, failed)
    assert req.text == "All actors: {'Jonny Sins': {'id': '001', 'username': 'Jonny_Big_Dick_28', 'email': 'jonnysinsvkisku28@porn.cum', 'department': 'Anal Department', 'date_joined': '13.01.2004'}, 'Sasha Grey': {'id': '002', 'username': 'Sasha_Grey_House', 'email': 'sashagreyhouse13@porn.cum', 'department': 'Cook Cum Pie', 'date_joined': '15.06.2001'}, 'Ariana Marie': {'id': '003', 'username': 'Anna_Maria_000', 'email': 'arianafishmaster000@porn.cum', 'department': 'Ass Accept', 'date_joined': '27.02.2005'}}"

