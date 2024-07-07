import streamlit as st
import calculations
import PyNite
from PyNite import FEModel3D
import matplotlib as plt

col1, col2 = st.columns(2)

with col1:
    st.header('Inputs')
    length = st.slider('Beam length', 1, 100)
    length_unit = st.selectbox('Units', ['mm', 'm'])

    force = st.slider('Distributed Load', -100, 100)
    force_unit = st.selectbox('Units', ['N', 'kN'])

moment_unit = f'{force_unit}{length_unit}'

beam = calculations.calculate_beam(0, length, force)
beam.analyze()
left_support_reaction  = beam.Nodes['N1'].RxnFY['Combo 1']
right_support_reaction = beam.Nodes['N2'].RxnFY['Combo 1']

max_shear = beam.Members['M1'].max_shear('Fy', 'Combo 1')
max_moment = beam.Members['M1'].max_moment('Mz', 'Combo 1')

shear_array = beam.Members['M1'].shear_array('Fy', 100, 'Combo 1')
moment_array = beam.Members['M1'].moment_array('Mz', 100, 'Combo 1')
fig_shear = calculations.plot_results(shear_array)
fig_moment = calculations.plot_results(moment_array*-1)


with col2:
    st.header('Output')
    st.write(f'Max shear: {max_shear} {force_unit}')
    st.write(f'Max moment: {max_moment} {moment_unit}')
    st.pyplot(fig_shear)
    st.pyplot(fig_moment)

