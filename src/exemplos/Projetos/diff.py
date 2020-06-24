#  -*- coding: utf-8 -*-
#    @package: diff.py
#     @author: Guilherme N. Ramos (gnramos@unb.br)
# @disciplina: Algoritmos e Programação de Computadores
#
# Mostra as diferenças entre os arquivos utilizando o comando diff.


from argparse import ArgumentParser
import os
import subprocess


def project_dir(project_dir):
    u"""Verifica o diretório do projeto."""
    if not os.path.exists(project_dir):
        raise ValueError('"{}" não é um diretório válido.'.format(project_dir))
    return project_dir


def parse_args():
    u"""Processa os argumentos fornecidos."""
    ap = ArgumentParser(description='Apresenta a evolução do código de um '
                                    'projeto.')
    ap.add_argument('projeto', type=project_dir,
                    help='Nome do projeto cujos arquivos devem ser '
                         'processados.')
    ap.add_argument('-e', '--extensao',
                    help='Extensão dos arquivos a processar.',
                    default='c', choices=['c', 'py'])
    return ap.parse_args()


def terminal(cmd):
    u"""Executa o comando dado no terminal."""
    # ************
    # * ATENÇÃO! *
    # ************
    # A instrução "run" faz o sistema operacional executar o comando
    # fornecido como argumento, e isto pode ser *MUITO* perigoso.
    subprocess.run('clear && {}'.format(cmd), shell=True)


def diff_files(projeto, extensao):
    u"""Mostra a diferença entre arquivos de código do projeto.

    Itera pela lista de todos os arquivos de código do projeto, em ordem
    alfabética, e mostra a diferença entre eles com o comando diff.
    """
    files = []
    with os.scandir(projeto) as it:
        files = sorted(entry.path
                       for entry in it
                       if entry.is_file() and entry.name.endswith(extensao))

    if files:
        terminal('cat {}'.format(files[0]))
        input(f'\n [Enter] para continuar (0/{len(files)- 1})...')

        x = 1
        while 0 < x < len(files):
            terminal(f'diff {files[x - 1]} {files[x]}')
            s = input(f'\n [Enter] para continuar ({x}/{len(files) - 1})')
            x += 1 if s == '' else -1

        # terminal('cat {}'.format(files[-1]))


if __name__ == '__main__':
    args = parse_args()
    diff_files(args.projeto, args.extensao)


# A função "run" (definida em subprocess) é usada no seu programa para
# solicitar que o sistema operacional execute um comando. Neste exemplo, foi
# usada para dizer ao sistema operacional que execute o comando "diff".
#
# Imagine se este programa apagasse todos os seus arquivos, ou enviasse e-mails
# com todos os seus dados pessoais (que deveriam ser privados) ou que fosse um
# ransomware (https://pt.wikipedia.org/wiki/Ransomware) ou pior...
#
# ********************************
# * O ideal é evitar utilizá-la. *
# ********************************
