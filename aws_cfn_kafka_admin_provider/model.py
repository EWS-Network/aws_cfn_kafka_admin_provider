# generated by datamodel-codegen:
#   filename:  aws-cfn-kafka-admin-provider-schema.json
#   timestamp: 2021-04-05T10:20:23+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, constr
from typing_extensions import Literal


class ReplicationFactor(BaseModel):
    __root__: int = Field(..., description="Kafka topic replication factor")


class Topic(BaseModel):
    Name: constr(regex=r"^[a-zA-Z0-9_.-]+$", min_length=1) = Field(
        ..., description="Kafka topic name"
    )
    PartitionsCount: int = Field(
        ..., description="Number of partitions for the new Kafka topic"
    )
    ReplicationFactor: Optional[ReplicationFactor] = None
    Settings: Optional[Dict[str, Any]] = None


class Model(BaseModel):
    BootstrapServers: str
    SecurityProtocol: Optional[
        Literal["PLAINTEXT", "SSL", "SASL_PLAINTEXT", "SASL_SSL"]
    ] = Field("PLAINTEXT", description="Kafka Security Protocol.")
    SASLMechanism: Optional[
        Literal["PLAIN", "GSSAPI", "OAUTHBEARER", "SCRAM-SHA-256", "SCRAM-SHA-512"]
    ] = Field("PLAIN", description="Kafka SASL mechanism for Authentication")
    SASLUsername: Optional[str] = Field(
        None, description="Kafka SASL username for Authentication"
    )
    SASLPassword: Optional[str] = Field(
        None, description="Kafka SASL password for Authentication"
    )
    FunctionName: Optional[str] = Field(
        None,
        description="Name or ARN of the Lambda function to use for Custom::KafkaTopic",
    )
    ReplicationFactor: Optional[ReplicationFactor] = None
    Topics: List[Topic]