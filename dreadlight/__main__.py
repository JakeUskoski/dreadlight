import argparse
import os

from dreadlight.displays import inv_display, shop_display

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(prog='Gladiators', description='A terminal-based background RPG to procrastinate with')
parser.add_argument('-v', '--verbose', action='store_true', help='show greater detail in output')
parser.add_argument('--version', action='version', version='%(prog)s 2.0')

subparsers = parser.add_subparsers(help='activities', dest='command')

shop_parser = subparsers.add_parser('shop')
shop_group = shop_parser.add_mutually_exclusive_group()
shop_group.add_argument('-l', '--list', action='store_true', help='List all items available for purchase in the shop')
shop_group.add_argument('-b', '--buy', metavar='item', nargs='+', help='''
                        Buy items from the shop.
                        Enter either their positions in the shop or their full names.
                        ''')
shop_group.add_argument('-s', '--sell', metavar='"item"', nargs='+', help='''
                        Sell all items listed.
                        Enter either their positions in the shop or their full names.
                        ''')
shop_group.add_argument('-d', '--details', metavar='"item"', nargs=1, help='''
                        See details of an item in the stop.
                        Enter either a position in the shop (or equipment) or the full name of the item.
                        ''')
shop_group.add_argument('-c', '--compare', metavar='"item"', nargs=2, help='''
                        Compare an item in the stop with currently equipped gear.
                        Enter either the positions in the shop (or equipment) or the full names of the items
                        ''')

inventory_parser = subparsers.add_parser('inv')
inv_group = inventory_parser.add_mutually_exclusive_group()
inv_group.add_argument('-l', '--list', action='store_true', help='''
                        List all items in the inventory.
                        Equipped items are signified with (e).
                        ''')
inv_group.add_argument('-t', '--toss', metavar='"item"', nargs='+', help='''
                        Toss away items in inventory permanently.
                        Enter either their positions in the inventory or their full names.
                        ''')
inv_group.add_argument('-d', '--details', metavar='"item"', nargs=1, help='''
                        See details of an item in the inventory.
                        Enter either a position in the inventory or the full name of the item.
                        ''')
inv_group.add_argument('-c', '--compare', metavar='"item"', nargs=2, help='''
                        Compare two items in the inventory.
                        Enter either the positions in the inventory or the full names of the items.
                        ''')
inv_group.add_argument('-e', '--equip', metavar='"item"', nargs=1, help='''
                        Equip item in the inventory.
                        Enter either the position in the inventory or the full name of the item to equip.
                        ''')
inv_group.add_argument('-u', '--unequip', metavar='"item"', nargs=1, help='''
                        Unequip item currently equipped.
                        Enter either the position in the inventory or the full name of the item to unequip.
                        ''')

if __name__ == '__main__':
    args = vars(parser.parse_args())
    print(args)
    if args['command'] == 'inv':
        if args['list'] is True:
            inv_display.inv_list()
        elif args['details'] is not None:
            inv_display.inv_details(args['details'][0])
        elif args['compare'] is not None:
            inv_display.inv_compare(args['compare'][0], args['compare'][1])
        elif args['toss'] is not None:
            inv_display.inv_toss(args['toss'])
        elif args['equip'] is not None:
            inv_display.inv_equip(args['equip'][0])
        elif args['unequip'] is not None:
            inv_display.inv_unequip(args['unequip'][0])
    elif args['command'] == 'shop':
        if args['list'] is True:
            shop_display.shop_list()
        elif args['details'] is not None:
            shop_display.shop_details(args['details'][0])
        elif args['buy'] is not None:
            shop_display.shop_buy(args['buy'])
        elif args['sell'] is not None:
            shop_display.shop_sell(args['sell'])
        elif args['compare'] is not None:
            shop_display.shop_compare(args['compare'][0], args['compare'][1])