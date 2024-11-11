#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python e Gtk
# Prof. Douglas Machado Tavares

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Aplicacao:
    """ Define a interface da Aplicação """


    def __init__(self):
        """ __init__() -> instância de Aplicação """
        self.gui = Gtk.Builder()
        self.gui.add_from_file("dados/interface/acai_glade.glade")
        self.gui.connect_signals(self)
        jnl = self.gui.get_object("jnl")
        jnl.show_all()


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        print(78*"-")
        print("\nObrigado por usar o Açaí Super 10 ;-)")
        raise SystemExit()


    def enviar(self, componente=None, dados=None):
        """ Envia o pedido """
        cxv_tamanho = self.gui.get_object("cxv_tamanho")
        cxv_recipiente = self.gui.get_object("cxv_recipiente")
        cxv_adicionais = self.gui.get_object("cxv_adicionais")

        pedido = ""
        for bte in cxv_tamanho:
            if bte.get_active():
                pedido = pedido + "Tamanho: {}\n".format(bte.get_label())

        for bte in cxv_recipiente:
            if bte.get_active():
                pedido = pedido + "Recipiente: {}\n".format(bte.get_label())

        pedido = pedido + "Adicionais: "
        for btv in cxv_adicionais:
            if btv.get_active():
                pedido = pedido + "{}, ".format(btv.get_label())

        pedido = pedido[:-2] + "."
        print(78*"-")
        print(pedido)


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
