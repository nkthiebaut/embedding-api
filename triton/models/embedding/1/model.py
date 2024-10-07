import json
import triton_python_backend_utils as pb_utils
from sentence_transformers import SentenceTransformer


class TritonPythonModel:
    def initialize(self, args):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def execute(self, requests):
        responses = []
        for request in requests:
            input_text = (
                pb_utils.get_input_tensor_by_name(request, "TEXT")
                .as_numpy()
                .item()
                .decode("utf-8")
            )
            embedding = self.model.encode(input_text)

            output_tensor = pb_utils.Tensor("EMBEDDING", embedding.astype("float32"))
            inference_response = pb_utils.InferenceResponse(
                output_tensors=[output_tensor]
            )
            responses.append(inference_response)
        return responses

    def finalize(self):
        self.model = None
