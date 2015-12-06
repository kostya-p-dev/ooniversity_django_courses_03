#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpRequest
from django.template import RequestContext, loader
from quadratic.forms import QuadraticForm
from django.shortcuts import redirect


def quadratic_results(request):
    discr = ''
    res = ''

    if request.method == "GET":
        form = QuadraticForm(request.POST)
        if form.is_valid():
            a = request.POST['a']
            b = request.POST['b']
            c = request.POST['c']

            d = int(b) ** 2 - 4 * int(a) * int(c)
            discr = u'Дискриминант: '+str(d)
            if d >= 0:
                import math
                dd = math.sqrt(d)
                x1 = ( -float(b) + float(dd) ) / (float(a) * 2)
                x2 = ( -float(b) - float(dd) ) / (float(a) * 2)

                x1 = round(x1, 1)
                x2 = round(x2, 1)

                if x1 != x2 :
                    res = u'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s' % (str(x1), str(x2))
                else:
                    res = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % str(x1)
            else:
                res = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'

    else:
        form = QuadraticForm()

    template = loader.get_template('quadratic/results.html')
    context = RequestContext(request, {
        'discr': discr,
        'res': res,
        'form': form,
    })
    return HttpResponse(template.render(context))
