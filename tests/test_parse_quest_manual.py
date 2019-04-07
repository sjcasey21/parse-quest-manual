#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `parse_quest_manual` package."""

import pytest

from parse_quest_manual import parse_quest_manual


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_parse_manual():
    armor = '''
    <table>
        <tbody>
          <tr>
            <td><p><strong>Name</strong></p></td>
            <td><p><strong>DT</strong></p></td>
            <td><p><strong>Value</strong></p></td>
            <td><p><strong>Weight</strong></p></td>
            <td><p><strong>Traits</strong></p></td>
          </tr>
          <tr>
            <td><p>Advanced radiation suit</p></td>
            <td><p>2 DT</p></td>
            <td><p>12 caps</p></td>
            <td><p>7 lbs.</p></td>
            <td><p>+4 rad res., <em>Bodysuit</em></p></td>
          </tr>
        </tbody>
    </table>'''
    helmets = '''
    <table>
        <tbody>
          <tr>
            <td><p><strong>Name</strong></p></td>
            <td><p><strong>DT</strong></p></td>
            <td><p><strong>Value</strong></p></td>
            <td><p><strong>Weight</strong></p></td>
            <td><p><strong>Traits</strong></p></td>
          </tr>
          <tr>
            <td><p>Baseball cap</p></td>
            <td><p>0 DT</p></td>
            <td><p>1 caps</p></td>
            <td><p>1 lbs.</p></td>
            <td><p>+1 Melee weapons</p></td>
          </tr>
        </tbody>
    </table>'''
    source = '''
    <h2>something</h2>
    <p>some stuff before the items</p>
    <h2><a id="_lkjaslkdjflkj"></a>Chapter 15: Item Lists</h2>
    <h3>Armor Sets</h3>
    <h5>Special armors</h5>
    {}
    <h3>Helmets</h3>
    <h4>Hats</h4>
    {}
    <h4>Light Helmets</h4>
    <h5>Recon</h5>
    {}
    <p>some descriptions</p>
    <h4>some sub types</h4>
    <h1>a different section</h1>'''.format(armor, helmets, helmets)

    assert parse_quest_manual.parse_manual(source) == [
        {
            'category':
            'armor sets',
            'content': [{
                'subtype':
                'special armors',
                'items': [{
                    'name': 'advanced radiation suit',
                    'dt': 2,
                    'value': 12,
                    'weight': 7,
                    'traits': ['+4 rad res', 'bodysuit']
                }]
            }]
        },
        {
            'category':
            'helmets',
            'content': [
                {
                    'type':
                    'hats',
                    'items': [
                        {
                            'name': 'baseball cap',
                            'dt': 0,
                            'value': 1,
                            'weight': 1,
                            'traits': ['+1 melee weapons']
                        },
                    ]
                },
                {
                    'type':
                    'light helmets',
                    'subtype':
                    'recon',
                    'items': [
                        {
                            'name': 'baseball cap',
                            'dt': 0,
                            'value': 1,
                            'weight': 1,
                            'traits': ['+1 melee weapons']
                        },
                    ]
                },
            ]
        },
    ]
