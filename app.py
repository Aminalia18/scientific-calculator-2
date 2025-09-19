import streamlit as st
import sympy as sp

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮")

st.title("🧮 Scientific Calculator")

# Input expression
expression = st.text_input("Enter a mathematical expression (e.g. sin(pi/2) + sqrt(16)):")

if st.button("Calculate"):
    try:
        # Parse and evaluate with sympy
        result = sp.sympify(expression).evalf()
        st.success(f"✅ Result: {result}")
    except Exception as e:
        st.error(f"❌ Error: {e}")

st.markdown("---")
st.caption("Powered by Streamlit + Sympy")
