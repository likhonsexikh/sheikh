#!/usr/bin/env python3
# scripts/manage_endpoints.py

import argparse
import os
import sys
from huggingface_hub import (
    create_inference_endpoint,
    get_inference_endpoint,
    list_inference_endpoints,
    InferenceEndpointError,
)

def main():
    """
    A command-line tool to manage Hugging Face Inference Endpoints.
    """
    parser = argparse.ArgumentParser(
        description="Manage Hugging Face Inference Endpoints.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- Create command ---
    parser_create = subparsers.add_parser("create", help="Create a new Inference Endpoint.")
    parser_create.add_argument("name", type=str, help="Name of the endpoint.")
    parser_create.add_argument("--repo", type=str, default="gpt2", help="Repository ID on the Hub.")
    parser_create.add_argument("--vendor", type=str, default="aws", help="Cloud provider.")
    parser_create.add_argument("--region", type=str, default="us-east-1", help="Provider region.")
    parser_create.add_argument("--instance-size", type=str, default="x2")
    parser_create.add_argument("--instance-type", type=str, default="intel-icl")
    parser_create.add_argument("--type", type=str, default="protected", choices=["public", "protected", "private"])

    # --- List command ---
    parser_list = subparsers.add_parser("list", help="List all Inference Endpoints.")
    parser_list.add_argument("--namespace", type=str, help="Namespace (user or org). Defaults to you.")

    # --- Get command ---
    parser_get = subparsers.add_parser("get", help="Get details of a specific endpoint.")
    parser_get.add_argument("name", type=str, help="Name of the endpoint.")

    # --- Pause command ---
    parser_pause = subparsers.add_parser("pause", help="Pause a running endpoint.")
    parser_pause.add_argument("name", type=str, help="Name of the endpoint.")

    # --- Resume command ---
    parser_resume = subparsers.add_parser("resume", help="Resume a paused endpoint.")
    parser_resume.add_argument("name", type=str, help="Name of the endpoint.")

    # --- Delete command ---
    parser_delete = subparsers.add_parser("delete", help="Delete an endpoint.")
    parser_delete.add_argument("name", type=str, help="Name of the endpoint.")
    parser_delete.add_argument("-y", "--yes", action="store_true", help="Skip confirmation prompt.")

    args = parser.parse_args()

    # Check for HF_TOKEN
    if not os.environ.get("HF_TOKEN"):
        print("❌ Error: HF_TOKEN environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    try:
        if args.command == "create":
            print(f"Creating endpoint '{args.name}'...")
            endpoint = create_inference_endpoint(
                name=args.name,
                repository=args.repo,
                vendor=args.vendor,
                region=args.region,
                instance_size=args.instance_size,
                instance_type=args.instance_type,
                type=args.type,
                framework="pytorch",
                task="text-generation",
                accelerator="cpu",
            )
            print("⏳ Waiting for endpoint to be ready (this can take a few minutes)...")
            endpoint.wait()
            print(f"✅ Endpoint '{args.name}' is running at: {endpoint.url}")
            print(endpoint)

        elif args.command == "list":
            endpoints = list_inference_endpoints(namespace=args.namespace)
            if not endpoints:
                print("No endpoints found.")
                return
            for endpoint in endpoints:
                print(f"- {endpoint.name:<30} Status: {endpoint.status:<15} Repo: {endpoint.repository}")

        elif args.command == "get":
            endpoint = get_inference_endpoint(args.name)
            print(endpoint)

        elif args.command == "pause":
            print(f"Pausing endpoint '{args.name}'...")
            endpoint = get_inference_endpoint(args.name).pause()
            print(f"✅ Endpoint '{args.name}' is now {endpoint.status}.")

        elif args.command == "resume":
            print(f"Resuming endpoint '{args.name}'...")
            endpoint = get_inference_endpoint(args.name).resume()
            print(f"✅ Endpoint '{args.name}' is now {endpoint.status}.")

        elif args.command == "delete":
            if not args.yes:
                print(f"⚠️ Are you sure you want to delete endpoint '{args.name}'? This is irreversible.")
                confirm = input("Type 'yes' to confirm: ")
                if confirm.lower() != "yes":
                    print("Deletion cancelled.")
                    sys.exit(0)

            print(f"Deleting endpoint '{args.name}'...")
            get_inference_endpoint(args.name).delete()
            print(f"✅ Endpoint '{args.name}' deleted.")

    except InferenceEndpointError as e:
        print(f"❌ An API error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)

if __name__ == "__main__":
    main()
