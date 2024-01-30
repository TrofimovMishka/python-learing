from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes


table_test = ColorTable(theme=Themes.OCEAN, padding_width=10)
table_test.field_names = ["Keycloak", "LDAP Attribute"]

rows_test = [
    ["email", "mail"],
    ["first name", "givenName"],
    ["full name", "cn"],
    ["phone", "telephoneNumber"],
    ["username", "sAMAccountName"]
]

table_test.add_rows(rows_test)

table_prod = PrettyTable(padding_width=10)
table_prod.title = "Mapping on PROD env."

table_prod.field_names = ["Keycloak", "LDAP Attribute"]

rows_prod = [
    ["email", "mail"],
    ["first name", "givenName"],
    ["full name", "displayName"],
    ["phone", "telephoneNumber"],
    ["username", "sAMAccountName"]
]

table_prod.add_rows(rows_prod)

print(table_test)
print(table_prod)
