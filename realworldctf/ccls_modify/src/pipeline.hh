#pragma once

#include "lsp_diagnostic.h"
#include "method.h"
#include "query.h"

#include <string>
#include <unordered_map>
#include <vector>

struct GroupMatch;
struct VFS;
struct Project;
struct WorkingFiles;
struct lsBaseOutMessage;

class DiagnosticsPublisher {
  std::unique_ptr<GroupMatch> match_;
  int64_t nextPublish_ = 0;
  int frequencyMs_;

 public:
  void Init();
  void Publish(WorkingFiles* working_files,
               std::string path,
               std::vector<lsDiagnostic> diagnostics);
};

namespace ccls::pipeline {

    std::unique_ptr<IndexFile> RawCacheLoadHack();

void Init();
void LaunchStdin();
void LaunchStdout();
void Indexer_Main(DiagnosticsPublisher* diag_pub,
                  VFS* vfs,
                  Project* project,
                  WorkingFiles* working_files);
void MainLoop();

void Index(const std::string& path,
           const std::vector<std::string>& args,
           bool is_interactive,
           lsRequestId id = {});

std::optional<std::string> LoadCachedFileContents(const std::string& path);
void WriteStdout(MethodType method, lsBaseOutMessage& response);
}
