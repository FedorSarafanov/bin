#!/usr/bin/env wolframscript
(* ::Package:: *)

z=Function[{t,r},1+r*Exp[I*t]]
w=Function[z,2*I*z/(z+3)]


ParametricPlot[{{Re[z[t,r]],Im[z[t,r]]},{Re[w[z[t,r]]],Im[w[z[t,r]]]}},{t,0,2*Pi}, {r,0,2}, PlotStyle->{Red,Black}]
