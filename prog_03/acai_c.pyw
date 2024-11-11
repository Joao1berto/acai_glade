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
        #jnl = Gtk.Window()
        #jnl.connect("delete-event", self.sair)
        #jnl.set_border_width(10)c
        #jnl.set_title("Açaí é tudo de bom ;-)")
        #jnl.set_size_request(400, -1)

        #cxv = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
        #              homogeneous=False, spacing=10)

        #cxh = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
        #              homogeneous=True, spacing=10)

        #cxv_esq = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
        #                  homogeneous=False, spacing=10)

        #cxv_dir = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
        #                  homogeneous=False, spacing=10)

        #msg = ("<span color='#800080' font='Bold 14'>"
        #       ".:: Acaí Super 10 ::."
        #       "</span>")

        #rtl_acai = Gtk.Label(label=msg, use_markup=True)
        #cxv.add(rtl_acai)c
        #cxv.pack_start(cxh, True, True, 0)
        #cxh.add(cxv_esq)
        #cxh.add(cxv_dir)

        #cxv_tamanho = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
        #                      homogeneous=False, spacing=5)
        #cxv_tamanho.set_border_width(5)

        #qdr_tamanho = Gtk.Frame(label="Tamanho:")
        #qdr_tamanho.add(cxv_tamanho)
        #cxv_esq.add(qdr_tamanho)

        #cxv_recipiente = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
        #                         homogeneous=False, spacing=5)
        #cxv_recipiente.set_border_width(5)

        #qdr_recipiente = Gtk.Frame(label="Recipiente:")
        #qdr_recipiente.add(cxv_recipiente)
        #cxv_esq.add(qdr_recipiente)

        #bte_450 = Gtk.RadioButton(group=None, label="450 ml")
        #bte_300 = Gtk.RadioButton(group=bte_450, label="300 ml")
        #bte_600 = Gtk.RadioButton(group=bte_450, label="600 ml")
        #bte_700 = Gtk.RadioButton(group=bte_450, label="700 ml")

        #cxv_tamanho.add(bte_300)
        #cxv_tamanho.add(bte_450)
        #cxv_tamanho.add(bte_600)
        #cxv_tamanho.add(bte_700)

        #bte_copo = Gtk.RadioButton(group=None, label="Copo")
        #bte_tigela = Gtk.RadioButton(group=bte_copo, label="Tigela")

        #cxv_recipiente.add(bte_copo)
        #cxv_recipiente.add(bte_tigela)

        #cxv_adicionais = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
        #                         homogeneous=False, spacing=5)
        #cxv_adicionais.set_border_width(5)

        #qdr_adicionais = Gtk.Frame(label="Adicionais:")
        #qdr_adicionais.add(cxv_adicionais)
        #cxv_dir.add(qdr_adicionais)

        #btv_banana = Gtk.CheckButton(label="Banana")
        #btv_pacoca = Gtk.CheckButton(label="Paçoca")
        #btv_chocolate = Gtk.CheckButton(label="Chocolate")
        #btv_bis = Gtk.CheckButton(label="Bis")
        #btv_morango = Gtk.CheckButton(label="Morango")
        #btv_granola = Gtk.CheckButton(label="Granola")
        #btv_leite_em_po = Gtk.CheckButton(label="Leite em pó")

        #cxv_adicionais.add(btv_banana)
        #cxv_adicionais.add(btv_pacoca)
        #cxv_adicionais.add(btv_chocolate)
        #cxv_adicionais.add(btv_bis)
        #cxv_adicionais.add(btv_morango)
        #cxv_adicionais.add(btv_granola)
        #cxv_adicionais.add(btv_leite_em_po)

        #bt_enviar = Gtk.Button(label="_Enviar", use_underline=True)
        #bt_enviar.connect("clicked", self.enviar, [cxv_tamanho,
        #                  cxv_recipiente, cxv_adicionais])
        #cxv_dir.pack_end(bt_enviar, False, False, 0)

        #jnl.add(cxv)
        #jnl.show_all()


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicação """
        Gtk.main_quit()
        print(78*"-")
        print("\nObrigado por usar o Açaí Super 10 ;-)")
        raise SystemExit()


    def enviar(self, componente=None, dados=None):
        """ Envia o pedido """
        cxv_tamanho = dados[0]
        cxv_recipiente = dados[1]
        cxv_adicionais = dados[2]

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
