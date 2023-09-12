"""
Запишите словарь в yaml файл
"""
import yaml
to_yaml = {
   'access': ['switchport mode access',
              'switchport access vlan',
              'switchport nonegotiate',
              'spanning-tree portfast',
              'spanning-tree bpduguard enable'],
   'trunk': ['switchport trunk encapsulation dot1q',
             'switchport mode trunk',
             'switchport trunk native vlan 999',
             'switchport trunk allowed vlan'],
}
with open('sw_temlates.yaml', 'w') as f:
    yaml.dump(to_yaml, f)