import streamlit as st

def calculate_emi(principal, annual_interest_rate, tenure_years):
    """
    Calculate EMI (Equated Monthly Installment).

    :param principal: Principal loan amount
    :param annual_interest_rate: Annual interest rate (in percentage)
    :param tenure_years: Tenure in years
    :return: EMI amount
    """
    # Convert annual interest rate to monthly and tenure to months
    monthly_interest_rate = annual_interest_rate / (12 * 100)
    tenure_months = tenure_years * 12

    # EMI calculation formula
    if monthly_interest_rate == 0:
        emi = principal / tenure_months
    else:
        emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_months) / \
              ((1 + monthly_interest_rate) ** tenure_months - 1)
    
    return emi

def main():
    st.title("EMI Calculator")

    st.sidebar.header("Loan Details RINKU")

    # User inputs
    principal = st.sidebar.number_input("Principal Amount (Rs.)", min_value=0.0, format="%.2f")
    annual_interest_rate = st.sidebar.number_input("Annual Interest Rate (%)", min_value=0.0, format="%.2f")
    tenure_years = st.sidebar.number_input("Tenure (Years)", min_value=1, format="%d")

    if st.sidebar.button("Calculate EMI"):
        emi = calculate_emi(principal, annual_interest_rate, tenure_years)
        st.write(f"**Principal Amount:** ${principal:,.2f}")
        st.write(f"**Annual Interest Rate:** {annual_interest_rate:.2f}%")
        st.write(f"**Tenure:** {tenure_years} years")
        st.write(f"**EMI Amount:** ${emi:,.2f}")

if __name__ == "__main__":
    main()
