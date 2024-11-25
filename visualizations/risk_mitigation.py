import streamlit as st
import pandas as pd

# Dropdowns for attack types and vehicle components
st.sidebar.header("Risk Mitigation Controls")
attack_type = st.sidebar.selectbox(
    "Select Attack Type",
    ["DoS", "Spoofing", "Fuzzy", "Replay"]
)
component = st.sidebar.selectbox(
    "Select Vehicle Component",
    ["ECU", "Sensor", "CAN Bus", "Actuator"]
)

# Display selected items
st.header(f"Risk Mitigation Strategies for {attack_type} on {component}")

# Risk mitigation strategies
strategies = {
    "DoS": {
        "ECU": [
            "Implement rate-limiting mechanisms for incoming packets.",
            "Enhance ECU firmware with secure boot mechanisms.",
            "Install intrusion detection systems for real-time anomaly detection.",
            "Monitor and block unusual traffic patterns at the gateway."
        ],
        "Sensor": [
            "Use redundancy in sensors to cross-validate readings.",
            "Secure sensor communication with encryption protocols.",
            "Employ noise filters to mitigate signal jamming attacks.",
            "Monitor environmental patterns to detect outliers."
        ],
        "CAN Bus": [
            "Use message authentication codes (MACs) to verify CAN messages.",
            "Segment the CAN network for critical and non-critical systems.",
            "Deploy physical-layer security measures to detect anomalies.",
            "Limit the bandwidth allocated to suspicious nodes."
        ],
        "Actuator": [
            "Deploy actuator-specific encryption for secure control signals.",
            "Integrate fail-safe mechanisms to handle unexpected actuator behavior.",
            "Continuously monitor actuator performance and diagnose faults.",
            "Isolate critical actuators from external network access."
        ],
    },
    "Spoofing": {
        "ECU": [
            "Implement strong authentication protocols for communication.",
            "Use cryptographic signatures to verify the integrity of messages.",
            "Monitor message patterns to detect unusual communication behavior.",
            "Apply firmware updates to address known vulnerabilities."
        ],
        "Sensor": [
            "Encrypt data transmitted from sensors to prevent tampering.",
            "Use timestamp verification to prevent replay of old sensor data.",
            "Validate sensor outputs using machine learning models for anomalies.",
            "Employ sensor fusion techniques to cross-check readings."
        ],
        "CAN Bus": [
            "Implement message authentication for CAN bus messages.",
            "Use dynamic identifiers for critical messages to prevent spoofing.",
            "Regularly audit CAN bus communication logs for irregularities.",
            "Segregate high-risk systems to prevent cascading effects of spoofing."
        ],
        "Actuator": [
            "Restrict control access to actuators to verified nodes only.",
            "Monitor control commands for unusual patterns or conflicts.",
            "Deploy tamper-resistant actuators with secure firmware.",
            "Log all actuator commands and responses for forensic analysis."
        ],
    },
    "Fuzzy": {
        "ECU": [
            "Monitor incoming data streams for random or malformed packets.",
            "Deploy data validation and error-checking protocols.",
            "Use rate-limiting to control the flow of incoming requests.",
            "Harden firmware to resist exploitation by malformed data."
        ],
        "Sensor": [
            "Filter out data anomalies using statistical techniques.",
            "Validate sensor inputs against historical and expected ranges.",
            "Deploy multiple sensors to identify inconsistent readings.",
            "Implement secure communication channels to block malformed data."
        ],
        "CAN Bus": [
            "Install real-time monitoring tools to detect fuzzed messages.",
            "Implement message filtering to drop malformed packets.",
            "Use machine learning models to classify and block fuzzy attacks.",
            "Regularly update CAN controller firmware to patch vulnerabilities."
        ],
        "Actuator": [
            "Limit actuator responses to predefined safe ranges.",
            "Implement error-handling mechanisms for invalid commands.",
            "Validate all incoming control signals before execution.",
            "Deploy redundant actuators to ensure consistent operation."
        ],
    },
    "Replay": {
        "ECU": [
            "Implement session tokens for secure communication.",
            "Validate timestamps to ensure data freshness.",
            "Use challenge-response authentication for command verification.",
            "Monitor traffic patterns to identify repeated messages."
        ],
        "Sensor": [
            "Embed unique identifiers in data packets to prevent reuse.",
            "Use temporal analysis to detect replayed data patterns.",
            "Encrypt sensor data with session-based keys.",
            "Log and review anomalies in sensor communication channels."
        ],
        "CAN Bus": [
            "Implement timestamp-based validation for CAN messages.",
            "Use rolling codes to secure critical messages.",
            "Analyze traffic for repeated message IDs within short intervals.",
            "Deploy anomaly detection systems on the CAN bus."
        ],
        "Actuator": [
            "Verify the freshness of control commands using timestamps.",
            "Limit the validity of control signals to specific timeframes.",
            "Use hash-based message authentication codes for verification.",
            "Log all actuator commands and investigate repeated signals."
        ],
    },
}

# Display the strategies
if attack_type in strategies and component in strategies[attack_type]:
    for idx, strategy in enumerate(strategies[attack_type][component], 1):
        st.markdown(f"{idx}. {strategy}")
else:
    st.warning("No specific strategies available for the selected combination.")

# Download the risk mitigation strategies
if st.sidebar.button("Download Strategies"):
    strategy_text = "\n".join(strategies[attack_type][component])
    st.download_button(
        label="Download Strategies",
        data=strategy_text,
        file_name=f"{attack_type}_{component}_strategies.txt",
        mime="text/plain"
    )